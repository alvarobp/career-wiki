#!/bin/bash

usage() {
    echo "Usage: $0 [--lang CODE] <youtube_url> [output_file] [browser]"
    echo ""
    echo "Downloads the transcript in the language actually spoken in the video."
    echo ""
    echo "  --lang CODE  Download captions in this language (ISO 639-1, e.g. en, es)"
    echo "               when the video has them, uploaded or auto-translated."
    echo "               Without it, or when the video has no captions in CODE,"
    echo "               the language spoken in the video is downloaded instead."
    echo ""
    echo "Example: $0 https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    echo "Example: $0 https://www.youtube.com/watch?v=dQw4w9WgXcQ transcript.txt"
    echo "Example: $0 https://www.youtube.com/watch?v=dQw4w9WgXcQ transcript.txt brave"
    echo "Example: $0 --lang en https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    echo ""
    echo "Supported browsers: chrome, firefox, safari, edge, opera, brave"
}

PREFERRED_LANG=""
POSITIONAL=()

while [ $# -gt 0 ]; do
    case "$1" in
        --lang)
            if [ -z "$2" ]; then
                echo "Error: --lang requires a language code" >&2
                exit 1
            fi
            PREFERRED_LANG="$2"
            shift 2
            ;;
        --lang=*)
            PREFERRED_LANG="${1#*=}"
            shift
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        -*)
            echo "Error: Unknown option: $1" >&2
            usage >&2
            exit 1
            ;;
        *)
            POSITIONAL+=("$1")
            shift
            ;;
    esac
done

if [ ${#POSITIONAL[@]} -eq 0 ]; then
    usage
    exit 1
fi

URL="${POSITIONAL[0]}"
OUTPUT_FILE="${POSITIONAL[1]:-transcript.txt}"
BROWSER="${POSITIONAL[2]:-brave}"

# Captions are downloaded here first so that a rejected attempt never clobbers a
# usable one, and so nothing is left behind next to the transcript.
WORK_DIR=$(mktemp -d "${TMPDIR:-/tmp}/yt-transcript.XXXXXX") || exit 1
trap 'rm -rf "$WORK_DIR"' EXIT

# The download method that worked for this video, reused across caption requests.
WORKING_METHOD=""

# Methods to try, in order of preference:
#   - cookies from the browser
#   - android_vr player client, which doesn't require a PO Token for auto-captions
#   - web player client, to bypass some restrictions
#   - a different user agent
#   - no special options (sometimes works)
METHODS=(
    "yt-dlp --cookies-from-browser $BROWSER|cookies from $BROWSER"
    "yt-dlp --extractor-args youtube:player_client=android_vr|android_vr player client"
    "yt-dlp --extractor-args youtube:player_client=web|web player client"
    "yt-dlp --user-agent 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'|custom user agent"
    "yt-dlp|basic method"
)

# "es-US" and "ES" both mean the same thing as "es" for our purposes.
normalize_lang() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | cut -d- -f1
}

# The language a downloaded VTT is in, per its own header. Empty if unknown.
vtt_language() {
    [ -f "$1" ] || return 0
    grep -m1 '^Language:' "$1" | sed 's/^Language:[[:space:]]*//' | tr -d '\r'
}

first_vtt() {
    ls "$WORK_DIR/$1".*.vtt 2>/dev/null | head -1
}

try_download() {
    local cmd="$1"
    local method="$2"
    local slot="$3"
    local sub_langs="$4"
    local auto_flag="$5"

    echo "Trying method: $method"
    # Remove any stale VTT from a previous attempt so the existence check is meaningful
    rm -f "$WORK_DIR/$slot".*.vtt
    if $cmd --write-subs $auto_flag --sub-langs "$sub_langs" --skip-download --sub-format vtt --output "$WORK_DIR/$slot" "$URL" 2>/dev/null \
        && ls "$WORK_DIR/$slot".*.vtt >/dev/null 2>&1; then
        echo "✓ Success with $method"
        return 0
    else
        echo "✗ Failed with $method"
        return 1
    fi
}

# Runs the whole method chain for one set of caption languages. Pass "auto" to
# also accept YouTube's generated captions; anything else restricts the download
# to subtitles a human uploaded.
fetch_captions() {
    local slot="$1"
    local sub_langs="$2"
    local auto_flag=""
    local methods=("${METHODS[@]}")
    local entry

    [ "$3" = "auto" ] && auto_flag="--write-auto-subs"

    # Once a method has worked for this video the rest add nothing: they exist to
    # get past extraction failures, not to conjure captions the video lacks.
    [ -n "$WORKING_METHOD" ] && methods=("$WORKING_METHOD")

    echo ""
    echo "Requesting captions: $sub_langs"
    for entry in "${methods[@]}"; do
        if try_download "${entry%%|*}" "${entry##*|}" "$slot" "$sub_langs" "$auto_flag"; then
            WORKING_METHOD="$entry"
            return 0
        fi
    done
    return 1
}

# Function to clean transcript
clean_transcript() {
    local vtt_file="$1"
    local dest="$2"

    echo "Cleaning transcript from: $vtt_file"

    # Clean the VTT file
    sed -E '
        /^[0-9]{2}:[0-9]{2}:[0-9]{2}/d
        /^WEBVTT/d
        /^Kind:/d
        /^Language:/d
        /^$/d
        s/<[^>]*>//g
        s/align:start position:[0-9]+%//g
        s/&amp;/\&/g
        s/&lt;/</g
        s/&gt;/>/g
    ' "$vtt_file" | \
    # Remove duplicate lines and clean up
    awk '!seen[$0]++' | \
    # Remove lines that are just whitespace
    sed '/^[[:space:]]*$/d' > "$dest"

    echo "Clean transcript saved as: $dest"
}

echo "Downloading transcript from: $URL"
echo "Output file: $OUTPUT_FILE"
[ -n "$PREFERRED_LANG" ] && echo "Preferred language: $PREFERRED_LANG"

CHOSEN_VTT=""
# Whether the chosen captions are the ones spoken in the video, as opposed to
# subtitles someone wrote in another language.
IS_ORIGINAL=""

# YouTube auto-translates captions into every language it supports, so asking for
# a fixed language gets a machine translation of the audio rather than the audio
# itself. The generated track for the spoken language is the only one suffixed
# "-orig", so this regex picks it whatever language the video is in.
if fetch_captions orig ".*-orig" auto; then
    CHOSEN_VTT=$(first_vtt orig)
    IS_ORIGINAL=yes
fi

# Any captions in the requested language will do, whether someone uploaded them
# or YouTube translated them itself — both are a transcript in that language,
# which beats translating downstream. yt-dlp serves uploaded subtitles ahead of
# generated ones when a language has both, so the better source still wins.
if [ -n "$PREFERRED_LANG" ] \
    && [ "$(normalize_lang "$(vtt_language "$CHOSEN_VTT")")" != "$(normalize_lang "$PREFERRED_LANG")" ]; then
    if fetch_captions preferred "$PREFERRED_LANG" auto; then
        CHOSEN_VTT=$(first_vtt preferred)
        IS_ORIGINAL=""
    fi
fi

# Videos captioned by hand and never auto-captioned have no "-orig" track at all.
# Whatever they do have is the only transcript there is, so it counts as the
# original unless it's a translation we specifically went looking for.
if [ -z "$CHOSEN_VTT" ] && fetch_captions any "all" manual; then
    if [ -n "$PREFERRED_LANG" ] && CHOSEN_VTT=$(first_vtt "any.$PREFERRED_LANG") && [ -n "$CHOSEN_VTT" ]; then
        IS_ORIGINAL=""
    else
        CHOSEN_VTT=$(first_vtt any)
        IS_ORIGINAL=yes
    fi
fi

if [ -z "$CHOSEN_VTT" ]; then
    echo ""
    echo "All methods failed. Possible solutions:"
    echo "1. Make sure you're logged into YouTube in your $BROWSER browser"
    echo "2. Try a different browser: ./$(basename $0) \"$URL\" \"$OUTPUT_FILE\" firefox"
    echo "3. Check if the video has captions available"
    echo "4. Update yt-dlp: pip install -U yt-dlp"
    exit 1
fi

TRANSCRIPT_LANG=$(normalize_lang "$(vtt_language "$CHOSEN_VTT")")
[ -n "$TRANSCRIPT_LANG" ] || TRANSCRIPT_LANG="unknown"

clean_transcript "$CHOSEN_VTT" "$OUTPUT_FILE"

# Which caption track this text came from, named the way YouTube names them:
# "es-orig" for the spoken language, "es" for written-by-hand subtitles. Callers
# use it to file the transcript under a name that says what's inside it.
TRANSCRIPT_TRACK="$TRANSCRIPT_LANG"
[ -n "$IS_ORIGINAL" ] && TRANSCRIPT_TRACK="${TRANSCRIPT_LANG}-orig"
echo "$TRANSCRIPT_TRACK" > "${OUTPUT_FILE}.track"

if [ -n "$IS_ORIGINAL" ]; then
    echo "Transcript language: $TRANSCRIPT_LANG (spoken in the video)"
else
    echo "Transcript language: $TRANSCRIPT_LANG (uploaded subtitles)"
fi
echo "Transcript downloaded successfully to: $OUTPUT_FILE"
