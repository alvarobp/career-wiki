#!/usr/bin/env python3
"""Helpers for wiki-add — JSON extraction, scoped edits, and link paths.

Subcommands:
  extract-json                        stdin -> first balanced JSON object on stdout
  apply-hunks <target> <hunks> <out>  apply scoped edits to a note
  relpath <to> <from>                 markdown link path from one note to another
  wrap <width> [indent] [hang]        stdin -> lines wrapped to width, each indented
  fold-figures <post.md> [captions]   bundle markdown -> numbered, described figures
  wire-images <note.md> <images-dir>  copy the images a note kept in, next to it
  index-link <section.md> <note.md> <title>   link a new note from its section page
"""
import json
import os
import re
import shutil
import sys
import textwrap

IMAGE_LINK = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")


def extract_json():
    """Pull the first balanced JSON object out of a model response.

    Models wrap JSON in prose or fences despite instructions, and the objects
    here are multi-line, so a brace counter that skips over string contents is
    the only reliable way to find the boundaries.
    """
    text = sys.stdin.read()
    start = text.find("{")
    if start == -1:
        sys.exit("no JSON object found in response")

    depth, in_string, escaped = 0, False, False
    for i in range(start, len(text)):
        ch = text[i]
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                candidate = text[start:i + 1]
                try:
                    json.loads(candidate)
                except ValueError as exc:
                    sys.exit("response contained malformed JSON: %s" % exc)
                sys.stdout.write(candidate)
                return
    sys.exit("JSON object in response was never closed")


def apply_hunks(target, hunks_path, out_path):
    """Apply anchor-based edits, touching only the lines around each anchor.

    Anchors are matched against the working copy before every hunk, so earlier
    insertions can't shift later ones, and a non-unique anchor is a hard error
    rather than an edit landing in an arbitrary spot.
    """
    with open(target) as handle:
        lines = handle.read().split("\n")
    with open(hunks_path) as handle:
        hunks = json.load(handle).get("hunks") or []
    if not hunks:
        sys.exit("no hunks to apply")

    for n, hunk in enumerate(hunks, 1):
        anchor = (hunk.get("anchor") or "").strip()
        if not anchor:
            sys.exit("hunk %d: missing anchor" % n)
        content = (hunk.get("content") or "").strip("\n")
        if not content:
            sys.exit("hunk %d: empty content" % n)
        position = hunk.get("position") or "after"

        matches = [i for i, line in enumerate(lines) if line.strip() == anchor]
        if not matches:
            sys.exit("hunk %d: anchor not found in %s: %r" % (n, target, anchor))
        if len(matches) > 1:
            sys.exit("hunk %d: anchor matches %d lines in %s, must be unique: %r"
                     % (n, len(matches), target, anchor))

        index = matches[0]
        block = content.split("\n")
        if position == "after":
            head, tail = lines[:index + 1], lines[index + 1:]
            while tail and not tail[0].strip():
                tail.pop(0)
            lines = head + [""] + block + ([""] if tail else []) + tail
        elif position == "before":
            head, tail = lines[:index], lines[index:]
            while head and not head[-1].strip():
                head.pop()
            lines = head + ([""] if head else []) + block + [""] + tail
        elif position == "replace":
            lines[index:index + 1] = block
        else:
            sys.exit("hunk %d: unknown position %r" % (n, position))

    with open(out_path, "w") as handle:
        handle.write("\n".join(lines))


def wrap(width, indent="", hang=""):
    """Wrap stdin for display inside a gum box.

    gum style sizes its border to the longest line it is handed and never wraps,
    so callers have to pre-wrap. fold(1) counts bytes, which mangles the em
    dashes and curly quotes the model writes; textwrap counts characters.
    Hyphen breaking stays off so kebab-case filenames survive intact.

    `hang` indents the continuation lines further, so a wrapped item reads as a
    continuation rather than as the next item in the list.
    """
    width = max(int(width), len(indent) + len(hang) + 10)
    lines = textwrap.wrap(sys.stdin.read().strip(), width=width,
                          initial_indent=indent, subsequent_indent=indent + hang,
                          break_on_hyphens=False)
    if lines:
        sys.stdout.write("\n".join(lines) + "\n")


def fold_figures(post_path, captions_path=None):
    """Number every image in a bundle and fold its description in beside it.

    The planning and drafting steps run without tools, so they can only use an
    image if someone has already looked at it. Writing the description into the
    source as a quote under the link keeps the markdown link intact — a drafter
    that decides the figure belongs in the note copies that line verbatim, and
    wire_images does the rest.
    """
    with open(post_path) as handle:
        text = handle.read()

    described = {}
    if captions_path and os.path.exists(captions_path):
        try:
            with open(captions_path) as handle:
                for figure in json.load(handle).get("figures") or []:
                    described[os.path.basename(figure.get("file", ""))] = figure
        except ValueError:
            pass

    counter = [0]

    def replace(match):
        counter[0] += 1
        number, target = counter[0], match.group(2)
        figure = described.get(os.path.basename(target), {})
        caption = (figure.get("caption") or match.group(1) or "").strip()
        label = "Figure %d%s" % (number, " — " + caption if caption else "")
        out = "![%s](%s)" % (label, target)
        description = (figure.get("description") or "").strip()
        if description:
            weight = "" if figure.get("substantive", True) else " (decorative)"
            out += "\n> Figure %d%s: %s" % (number, weight, description)
        return out

    sys.stdout.write(IMAGE_LINK.sub(replace, text))


def wire_images(note_path, images_dir):
    """Copy the images a note references out of the bundle and next to the note.

    A note is only written once the drafts are accepted, so this runs at the end:
    whatever survived review gets its file copied into the category's images/
    folder and its link rewritten to the relative path the wiki already uses.
    Anything that isn't in the bundle is left alone and reported — a hallucinated
    filename should be visible, not silently swallowed.
    """
    with open(note_path) as handle:
        text = handle.read()
    note_dir = os.path.dirname(os.path.abspath(note_path))
    copied = []

    def replace(match):
        alt, target = match.group(1), match.group(2)
        if "://" in target:
            return match.group(0)
        source = os.path.join(images_dir, os.path.basename(target))
        if not os.path.exists(source):
            print("image not in the bundle, link left as-is: %s" % target, file=sys.stderr)
            return match.group(0)
        name = os.path.basename(source)
        os.makedirs(os.path.join(note_dir, "images"), exist_ok=True)
        shutil.copyfile(source, os.path.join(note_dir, "images", name))
        copied.append(name)
        return "![%s](./images/%s)" % (alt, name)

    rewritten = IMAGE_LINK.sub(replace, text)
    if rewritten != text:
        with open(note_path, "w") as handle:
            handle.write(rewritten)
    for name in copied:
        print(name)


INDEX_LINK = re.compile(r"^\[([^\]]+)\]\((?!\w+:)([^)\s]+)\)\s*$")


def index_link(section_path, note_path, title):
    """Add a new note to its section page's list of links.

    Every section in this wiki is a folder whose own page carries a plain list of
    links to what's inside it — the navigation the vault was imported with. A new
    note that nothing links to is invisible there, so it gets added to that list:
    beside the last link already in it, or at the end of the page when the section
    has no list yet.
    """
    target = os.path.relpath(os.path.abspath(note_path),
                             os.path.dirname(os.path.abspath(section_path)))
    with open(section_path) as handle:
        lines = handle.read().split("\n")

    last = None
    for i, line in enumerate(lines):
        match = INDEX_LINK.match(line)
        if match:
            if match.group(2) == target:
                return  # already listed
            last = i

    entry = "[%s](%s)" % (title, target)
    if last is None:
        while lines and not lines[-1].strip():
            lines.pop()
        lines += ["", entry, ""]
    else:
        lines[last + 1:last + 1] = ["", entry]

    with open(section_path, "w") as handle:
        handle.write("\n".join(lines))
    print(entry)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__.strip())
    command = sys.argv[1]
    if command == "extract-json":
        extract_json()
    elif command == "apply-hunks":
        if len(sys.argv) != 5:
            sys.exit("usage: helpers.py apply-hunks <target> <hunks.json> <out>")
        apply_hunks(*sys.argv[2:5])
    elif command == "relpath":
        if len(sys.argv) != 4:
            sys.exit("usage: helpers.py relpath <to> <from>")
        to_path, from_path = sys.argv[2], sys.argv[3]
        rel = os.path.relpath(to_path, os.path.dirname(from_path))
        sys.stdout.write(rel if rel.startswith(".") else "./" + rel)
    elif command == "wrap":
        if len(sys.argv) not in (3, 4, 5):
            sys.exit("usage: helpers.py wrap <width> [indent] [hang]")
        wrap(*sys.argv[2:5])
    elif command == "fold-figures":
        if len(sys.argv) not in (3, 4):
            sys.exit("usage: helpers.py fold-figures <post.md> [captions.json]")
        fold_figures(*sys.argv[2:4])
    elif command == "wire-images":
        if len(sys.argv) != 4:
            sys.exit("usage: helpers.py wire-images <note.md> <images-dir>")
        wire_images(sys.argv[2], sys.argv[3])
    elif command == "index-link":
        if len(sys.argv) != 5:
            sys.exit("usage: helpers.py index-link <section.md> <note.md> <title>")
        index_link(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        sys.exit("unknown subcommand: %s" % command)


if __name__ == "__main__":
    main()
