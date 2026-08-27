#!/bin/bash
# Ensures a cached transcript exists for the given YouTube URL.
# Usage: ensure_transcript <url> [preferred_lang]
#
# Transcripts are cached under tmp/, named after the language of their own text:
#   transcript-<id>-es-orig.txt  the language spoken in the video
#   transcript-<id>-es.txt       subtitles someone uploaded in that language
#   transcript-<id>-en.missing   checked once: the video has no real en captions
#
# On success, sets globals:
#   VIDEO_ID         - extracted video ID
#   TRANSCRIPT_FILE  - relative path under the project dir
#   TRANSCRIPT_LANG  - language of the transcript's text ("unknown" if undetected)
# Exits non-zero on invalid URL, download failure, or empty transcript.

TRANSCRIPT_MIN_BYTES=512

# "es-US", "ES" and "es-orig" all mean the same thing as "es" for our purposes.
_normalize_lang() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | cut -d- -f1
}

# A transcript that was only half-written is worse than none: re-fetch it.
_transcript_cached() {
    local size=0
    [ -f "$1" ] && size=$(wc -c < "$1" | tr -d ' ')
    [ "$size" -ge "$TRANSCRIPT_MIN_BYTES" ]
}

# The cached transcript in the language the video is spoken in, if any.
_cached_original() {
    local file
    for file in "tmp/transcript-${1}-"*-orig.txt; do
        _transcript_cached "$file" && { echo "$file"; return; }
    done
}

# The cached transcript whose text is in $2, whether that's because the video is
# in that language or because someone subtitled it into that language.
_cached_in_lang() {
    local file
    for file in "tmp/transcript-${1}-${2}-orig.txt" "tmp/transcript-${1}-${2}.txt"; do
        _transcript_cached "$file" && { echo "$file"; return; }
    done
}

ensure_transcript() {
    local url="$1"
    local preferred_lang
    local script_dir staging track

    preferred_lang=$(_normalize_lang "$2")
    script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    VIDEO_ID=$(echo "$url" | sed -n -e 's/.*[?&]v=\([^&]*\).*/\1/p' -e 's/.*youtu\.be\/\([^?]*\).*/\1/p')
    if [ -z "$VIDEO_ID" ]; then
        echo "Error: Could not extract video ID from URL: $url" >&2
        echo "Supported formats:" >&2
        echo "  - https://www.youtube.com/watch?v=VIDEO_ID" >&2
        echo "  - https://youtu.be/VIDEO_ID" >&2
        exit 1
    fi

    mkdir -p tmp

    if [ -z "$preferred_lang" ]; then
        TRANSCRIPT_FILE=$(_cached_original "$VIDEO_ID")
    else
        TRANSCRIPT_FILE=$(_cached_in_lang "$VIDEO_ID" "$preferred_lang")
        # Asked for this language before and the video hasn't got it, so there is
        # nothing to look for online: the original is the best source available.
        if [ -z "$TRANSCRIPT_FILE" ] && [ -f "tmp/transcript-${VIDEO_ID}-${preferred_lang}.missing" ]; then
            TRANSCRIPT_FILE=$(_cached_original "$VIDEO_ID")
        fi
    fi

    if [ -n "$TRANSCRIPT_FILE" ]; then
        echo "Using cached transcript: $TRANSCRIPT_FILE" >&2
    else
        # The final name depends on what language comes back, so land it on a
        # staging path first and file it once the downloader reports the track.
        staging="tmp/transcript-${VIDEO_ID}.partial"
        rm -f "$staging" "${staging}.track"

        echo "Downloading transcript for $VIDEO_ID..." >&2
        if ! "$script_dir/download-youtube-transcript.sh" \
            ${preferred_lang:+--lang "$preferred_lang"} "$url" "$staging" >/dev/null 2>&1; then
            rm -f "$staging" "${staging}.track"
            echo "Error: Failed to download transcript" >&2
            exit 1
        fi

        track=$(cat "${staging}.track" 2>/dev/null)
        [ -n "$track" ] || track="unknown"
        TRANSCRIPT_FILE="tmp/transcript-${VIDEO_ID}-${track}.txt"
        mv "$staging" "$TRANSCRIPT_FILE"
        rm -f "${staging}.track"

        # Remember a fruitless search so the next run doesn't repeat it.
        if [ -n "$preferred_lang" ] && [ "$(_normalize_lang "$track")" != "$preferred_lang" ]; then
            touch "tmp/transcript-${VIDEO_ID}-${preferred_lang}.missing"
        fi
    fi

    if ! _transcript_cached "$TRANSCRIPT_FILE"; then
        echo "Error: Transcript file is empty or does not exist" >&2
        exit 1
    fi

    track="${TRANSCRIPT_FILE#tmp/transcript-${VIDEO_ID}-}"
    TRANSCRIPT_LANG=$(_normalize_lang "${track%.txt}")
}
