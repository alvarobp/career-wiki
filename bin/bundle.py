#!/usr/bin/env python3
"""Turn a source into a bundle add.sh can plan from — its text and its images.

Subcommands:
  x <url> <outdir>       an X/Twitter post or Article, via the FxTwitter API
  local <path> <outdir>  a page saved by hand: markdown, or complete HTML

A bundle is a directory holding post.md (the source as markdown, with image links
pointing into images/), the image files themselves, and meta.json (title, author,
date) for the note's Source line. Everything downstream reads post.md, so both
subcommands have to produce the same shape.

post.md is written last, so a bundle that has one is a bundle that finished
downloading — which is what lets add.sh treat an existing directory as a cache.
"""
import html
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

# pbs.twimg.com and most sites serve fetchers a different (or no) response than
# browsers, so ask as a browser would.
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
TIMEOUT = 30


def fetch(url, binary=False):
    request = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        data = response.read()
    return data if binary else data.decode("utf-8", "replace")


def die(message):
    sys.exit("bundle.py: %s" % message)


def note(message):
    """Progress goes to stderr; stdout is reserved for the bundle's own output."""
    print(message, file=sys.stderr)


# --- Images -----------------------------------------------------------------

class Images:
    """Collects image references in document order, then fetches them.

    Rendering asks for a markdown link before anything has been downloaded, so
    the registry hands back the final path immediately and does the work later.
    Numbering follows first appearance, which is what makes "figure 3" mean the
    same thing in the markdown, in the filename and in a caption.
    """

    def __init__(self, outdir):
        self.dir = os.path.join(outdir, "images")
        self.items = []      # (source, filename) in document order
        self.seen = {}       # source -> filename

    def ref(self, source, alt="", base_dir=None):
        """Register an image (URL or local path) and return its markdown link."""
        if base_dir and not re.match(r"^(https?:|data:)", source):
            source = os.path.normpath(os.path.join(base_dir, source))
        if source.startswith("data:"):
            return ""
        if source not in self.seen:
            name = "%02d-%s" % (len(self.items) + 1, self._basename(source))
            self.seen[source] = name
            self.items.append((source, name))
        return "![%s](images/%s)" % (alt.replace("]", ")"), self.seen[source])

    @staticmethod
    def _basename(source):
        path = urllib.parse.urlparse(source).path if "://" in source else source
        base = re.sub(r"[^A-Za-z0-9._-]", "-", os.path.basename(path)) or "image"
        return base if re.search(r"\.[A-Za-z0-9]{2,4}$", base) else base + ".jpg"

    def collect(self):
        """Fetch or copy every registered image. Returns the number that failed.

        A missing image is not worth losing the text over: the reference stays in
        post.md, the caption pass skips what it cannot read, and the run goes on.
        """
        if not self.items:
            return 0
        os.makedirs(self.dir, exist_ok=True)
        failed = 0
        for index, (source, name) in enumerate(self.items, 1):
            target = os.path.join(self.dir, name)
            if os.path.exists(target):
                continue
            note("  image %d/%d — %s" % (index, len(self.items), name))
            try:
                if "://" in source:
                    with open(target, "wb") as handle:
                        handle.write(fetch(source, binary=True))
                else:
                    shutil.copyfile(source, target)
            except (OSError, urllib.error.URLError, urllib.error.HTTPError) as exc:
                note("  could not get %s — %s" % (source, exc))
                failed += 1
        return failed


def write_bundle(outdir, markdown, meta, images):
    failed = images.collect()
    with open(os.path.join(outdir, "meta.json"), "w") as handle:
        json.dump(meta, handle, indent=2)
    with open(os.path.join(outdir, "post.md"), "w") as handle:
        handle.write(markdown.rstrip() + "\n")
    got = len(images.items) - failed
    note("Bundle ready: %s (%d image%s)" % (outdir, got, "" if got == 1 else "s"))


# --- X / Twitter ------------------------------------------------------------

X_STATUS = re.compile(r"(?:x|twitter)\.com/([^/?#]+)/status(?:es)?/(\d+)", re.I)


def x_ids(url):
    match = X_STATUS.search(url)
    if not match:
        die("%s is not an X post URL" % url)
    return match.group(1), match.group(2)


def fx_tweet(handle, status_id):
    """Ask FxTwitter for a post. It reaches X's guest endpoints for us, which is
    what makes this work at all — x.com answers unauthenticated fetches with 402.
    """
    api = "https://api.fxtwitter.com/%s/status/%s" % (
        urllib.parse.quote(handle), status_id)
    try:
        payload = json.loads(fetch(api))
    except urllib.error.HTTPError as exc:
        die("FxTwitter answered %s for %s" % (exc.code, api))
    except (urllib.error.URLError, ValueError) as exc:
        die("could not reach FxTwitter (%s)" % exc)
    if payload.get("code") != 200 or not payload.get("tweet"):
        die("FxTwitter could not read that post: %s"
            % payload.get("message", "unknown error"))
    return payload["tweet"]


def utf16_markup(text, spans):
    """Wrap ranges of `text` in markers, with offsets counted as X counts them.

    Draft.js ranges are UTF-16 code unit offsets, so a single emoji earlier in a
    paragraph shifts every later offset by one against Python's per-character
    view. Splicing the markers into the UTF-16 encoding sidesteps the whole
    class of off-by-one that would otherwise bold the wrong words.
    """
    if not spans:
        return text
    data = text.encode("utf-16-le")
    units = [data[i:i + 2] for i in range(0, len(data), 2)]
    opens, closes = {}, {}
    # Longer spans open first and close last, so nesting stays balanced
    for start, end, prefix, suffix in sorted(spans, key=lambda s: (s[0], -s[1])):
        if start < 0 or end > len(units) or start >= end:
            continue
        opens.setdefault(start, []).append(prefix)
        closes.setdefault(end, []).insert(0, suffix)
    out = []
    for index in range(len(units) + 1):
        out.extend(m.encode("utf-16-le") for m in closes.get(index, []))
        out.extend(m.encode("utf-16-le") for m in opens.get(index, []))
        if index < len(units):
            out.append(units[index])
    return b"".join(out).decode("utf-16-le", "replace")


STYLE_MARKERS = {"Bold": "**", "Italic": "_", "Code": "`"}


def entity_index(entity_map):
    """entityMap comes back as [{key, value}]; older shapes use a plain object."""
    if isinstance(entity_map, dict):
        return {str(k): v for k, v in entity_map.items()}
    index = {}
    for entry in entity_map or []:
        if isinstance(entry, dict) and "key" in entry:
            index[str(entry["key"])] = entry.get("value") or {}
    return index


def block_text(block, entities):
    spans = []
    for style in block.get("inlineStyleRanges") or []:
        marker = STYLE_MARKERS.get(style.get("style"))
        if marker:
            start = style.get("offset", 0)
            spans.append((start, start + style.get("length", 0), marker, marker))
    for entity_range in block.get("entityRanges") or []:
        entity = entities.get(str(entity_range.get("key"))) or {}
        if entity.get("type") == "LINK":
            url = (entity.get("data") or {}).get("url")
            if url:
                start = entity_range.get("offset", 0)
                spans.append((start, start + entity_range.get("length", 0),
                              "[", "](%s)" % url))
    return utf16_markup(block.get("text") or "", spans)


def render_article(article, images):
    """Rebuild an X Article from its Draft.js blocks.

    The body arrives as typed blocks plus an entity map, with images referenced
    by media id and resolved through media_entities — so the images can only be
    put back where they belong by walking the blocks in order.
    """
    entities = entity_index((article.get("content") or {}).get("entityMap"))
    media = {str(entry.get("media_id")): entry
             for entry in article.get("media_entities") or []}

    lines = []
    cover = ((article.get("cover_media") or {}).get("media_info") or {}).get("original_img_url")
    if cover:
        lines += [images.ref(cover, "Cover"), ""]

    ordinal = 0
    for block in (article.get("content") or {}).get("blocks") or []:
        kind = block.get("type") or "unstyled"
        # List items are written without a trailing blank line, so whatever ends
        # a list has to open the gap itself or it merges into the last bullet
        if kind not in ("unordered-list-item", "ordered-list-item") and lines and lines[-1]:
            lines.append("")
        if kind == "atomic":
            for entity_range in block.get("entityRanges") or []:
                entity = entities.get(str(entity_range.get("key"))) or {}
                if entity.get("type") != "MEDIA":
                    continue
                for item in (entity.get("data") or {}).get("mediaItems") or []:
                    info = (media.get(str(item.get("mediaId"))) or {}).get("media_info") or {}
                    if info.get("original_img_url"):
                        lines += [images.ref(info["original_img_url"]), ""]
            continue

        text = block_text(block, entities)
        if not text.strip():
            continue
        header = re.match(r"header-(one|two|three|four|five|six)$", kind)
        if header:
            depth = ["one", "two", "three", "four", "five", "six"].index(header.group(1)) + 1
            lines += ["#" * depth + " " + text, ""]
        elif kind == "unordered-list-item":
            lines.append("- " + text)
        elif kind == "ordered-list-item":
            ordinal += 1
            lines.append("%d. %s" % (ordinal, text))
        elif kind == "blockquote":
            lines += ["> " + text, ""]
        elif kind == "code-block":
            lines += ["```", text, "```", ""]
        else:
            lines += [text, ""]
        if kind not in ("unordered-list-item", "ordered-list-item"):
            ordinal = 0
    return "\n".join(lines)


def render_media(tweet, images):
    lines = []
    for item in ((tweet.get("media") or {}).get("all") or []):
        if item.get("type") == "photo" and item.get("url"):
            lines += [images.ref(item["url"], item.get("altText") or ""), ""]
        elif item.get("url"):
            # Videos stay links: they are large, and nothing downstream can watch one
            lines += ["[%s: %s]" % (item.get("type", "media"), item["url"]), ""]
    return lines


def render_post(tweet, images):
    author = tweet.get("author") or {}
    lines = ["**@%s** (%s), %s" % (author.get("screen_name", "unknown"),
                                   author.get("name", ""), tweet.get("created_at", "")),
             "", (tweet.get("text") or (tweet.get("raw_text") or {}).get("text") or "").strip(), ""]
    lines += render_media(tweet, images)

    quote = tweet.get("quote")
    if quote:
        quoted_author = (quote.get("author") or {}).get("screen_name", "unknown")
        lines += ["> Quoting @%s: %s" % (quoted_author, (quote.get("text") or "").strip()), ""]
        lines += render_media(quote, images)
    return lines


def download_x(url, outdir):
    handle, status_id = x_ids(url)
    note("Downloading %s via FxTwitter..." % url)
    tweet = fx_tweet(handle, status_id)
    author = tweet.get("author") or {}
    article = tweet.get("article")
    images = Images(outdir)

    # A post linked mid-thread only makes sense with what it answers, and the
    # API hands us the parent chain one hop at a time. Bounded, because a long
    # reply chain is someone else's conversation, not this source.
    ancestors, parent, hops = [], tweet.get("replying_to_status"), 0
    while parent and hops < 8:
        previous = fx_tweet((tweet.get("replying_to") or handle), str(parent))
        ancestors.insert(0, previous)
        parent, hops = previous.get("replying_to_status"), hops + 1

    if article:
        title = article.get("title") or "X Article"
        date = (article.get("created_at") or tweet.get("created_at") or "")[:10]
        body = ["# %s" % title, "",
                "X Article by %s (@%s)%s" % (author.get("name", ""),
                                             author.get("screen_name", ""),
                                             ", " + date if date else ""),
                url, "", "---", "", render_article(article, images)]
    else:
        title = "Post by %s" % (author.get("name") or author.get("screen_name") or "unknown")
        date = tweet.get("created_at", "")
        body = ["# %s" % title, "", url, "", "---", ""]
        for ancestor in ancestors:
            body += ["### Earlier in the thread", ""] + render_post(ancestor, images)
        body += render_post(tweet, images)

    meta = {"kind": "article" if article else "post", "title": title, "url": url,
            "author": author.get("name") or "", "handle": author.get("screen_name") or "",
            "date": date}
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "raw.json"), "w") as raw:
        json.dump(tweet, raw, indent=2)
    write_bundle(outdir, "\n".join(body), meta, images)


# --- A page saved by hand ---------------------------------------------------

SKIPPED_TAGS = {"script", "style", "noscript", "svg", "nav", "footer", "header",
                "aside", "form", "iframe", "template"}
HEADINGS = {"h1": 1, "h2": 2, "h3": 3, "h4": 4, "h5": 5, "h6": 6}


class HtmlToMarkdown(HTMLParser):
    """Enough HTML to keep the shape of a saved article: headings, lists, links,
    emphasis, code and — the reason this path exists at all — images.
    """

    def __init__(self, images, base_dir):
        super().__init__(convert_charrefs=True)
        self.images, self.base_dir = images, base_dir
        self.out, self.skip_depth, self.list_stack = [], 0, []
        self.pre, self.link, self.title = False, None, ""
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag in SKIPPED_TAGS:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag == "title":
            self.in_title = True
        elif tag in HEADINGS:
            self.out.append("\n\n" + "#" * HEADINGS[tag] + " ")
        elif tag in ("p", "div", "section", "article", "br", "tr"):
            self.out.append("\n\n")
        elif tag in ("ul", "ol"):
            self.list_stack.append(tag)
            self.out.append("\n")
        elif tag == "li":
            marker = "1. " if self.list_stack[-1:] == ["ol"] else "- "
            self.out.append("\n" + "  " * max(len(self.list_stack) - 1, 0) + marker)
        elif tag == "blockquote":
            self.out.append("\n\n> ")
        elif tag == "pre":
            self.pre = True
            self.out.append("\n\n```\n")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("_")
        elif tag == "code" and not self.pre:
            self.out.append("`")
        elif tag == "a" and attributes.get("href"):
            self.link = attributes["href"]
            self.out.append("[")
        elif tag == "img" and attributes.get("src"):
            self.out.append("\n\n" + self.images.ref(attributes["src"],
                                                     attributes.get("alt", ""),
                                                     self.base_dir) + "\n\n")

    def handle_endtag(self, tag):
        if tag in SKIPPED_TAGS:
            self.skip_depth = max(self.skip_depth - 1, 0)
            return
        if self.skip_depth:
            return
        if tag == "title":
            self.in_title = False
        elif tag in ("ul", "ol") and self.list_stack:
            self.list_stack.pop()
        elif tag == "pre":
            self.pre = False
            self.out.append("\n```\n")
        elif tag in ("strong", "b"):
            self.out.append("**")
        elif tag in ("em", "i"):
            self.out.append("_")
        elif tag == "code" and not self.pre:
            self.out.append("`")
        elif tag == "a" and self.link:
            self.out.append("](%s)" % self.link)
            self.link = None
        elif tag in HEADINGS:
            self.out.append("\n")

    def handle_data(self, data):
        if self.in_title:
            self.title += data.strip()
            return
        if self.skip_depth:
            return
        self.out.append(data if self.pre else re.sub(r"\s+", " ", data))

    def markdown(self):
        text = html.unescape("".join(self.out))
        text = re.sub(r"[ \t]+\n", "\n", text)
        return re.sub(r"\n{3,}", "\n\n", text).strip()


def pick_source_file(path):
    """Accept the file itself, or the folder a browser saved it into."""
    if os.path.isfile(path):
        return path
    if not os.path.isdir(path):
        die("no such file or directory: %s" % path)
    for pattern in (r"\.(md|markdown)$", r"\.html?$", r"\.txt$"):
        matches = sorted(name for name in os.listdir(path) if re.search(pattern, name, re.I))
        if matches:
            return os.path.join(path, matches[0])
    die("found no .md, .html or .txt file in %s" % path)


def rewrite_local_images(markdown, images, base_dir):
    """Point a saved page's image links at the bundle, copying the files in."""
    def replace(match):
        alt, source = match.group(1), match.group(2).strip().split(" ")[0]
        return images.ref(source, alt, base_dir) or match.group(0)
    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace, markdown)


def download_local(path, outdir):
    source = pick_source_file(path)
    base_dir = os.path.dirname(os.path.abspath(source))
    note("Reading %s..." % source)
    images = Images(outdir)
    os.makedirs(outdir, exist_ok=True)

    with open(source, encoding="utf-8", errors="replace") as handle:
        raw = handle.read()

    if re.search(r"\.html?$", source, re.I):
        parser = HtmlToMarkdown(images, base_dir)
        parser.feed(raw)
        body, title = parser.markdown(), parser.title
    else:
        body = rewrite_local_images(raw, images, base_dir)
        heading = re.search(r"^#\s+(.+)$", body, re.M)
        title = heading.group(1).strip() if heading else os.path.basename(source)

    meta = {"kind": "saved-page", "title": title, "url": "", "author": "",
            "handle": "", "date": "", "saved_from": os.path.abspath(source)}
    write_bundle(outdir, body, meta, images)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__.strip())
    command, source, outdir = sys.argv[1:4]
    if command == "x":
        download_x(source, outdir)
    elif command == "local":
        download_local(source, outdir)
    else:
        die("unknown subcommand: %s" % command)


if __name__ == "__main__":
    main()
