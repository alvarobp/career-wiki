# Repository Guidelines

This file provides guidance to coding agents working in this repository.

## Repository Overview

This is a personal career wiki: everything worth keeping about software engineering practice,
originally exported from Notion and now kept as a plain-markdown Obsidian vault.

The repository root **is** the wiki. Everything at the top level is a section of it except:

- `bin/` — the command-line tooling that files new sources into the wiki
- `.claude/` — the `wiki-add` skill and the `/wiki:add` command
- `tmp/` — gitignored scratch space: downloaded bundles, transcripts, import scripts
- `README.md` — the index of top-level sections

## Wiki Conventions

**On disk everything is kebab-case ASCII; in the text titles keep their capitalisation.**

- `ai/context-engineering.md` holds `# Context Engineering` on its first line,
  and other notes link to it with the title as the label and the kebab-case path as the target.
- The H1 is the note's real title. The filename is the kebab-case form of it.

**A section is a folder, and its own page is the note inside it that shares its name.**

- `architecture/` is a section; `architecture/architecture.md` is its page.
- That page carries a list of bare links to everything in the section. That list is the navigation —
  a note nothing links to is a note nobody finds, so a new note is always added to it.
- A plain note is a file in its section's folder. A note that grows sub-notes of its own becomes a
  folder of its own name, with its content at `<name>/<name>.md`.
- No note lives at the repository root.

**Assets sit beside the note that uses them**: images in `images/`, everything else (PDFs,
archives) in `attachments/`.

**Note format.** New notes written from a source follow the format in
`.claude/skills/wiki-add/SKILL.md`: an H1, a `**Source:**` line, a summary, sections, and a closing
insight. Most existing notes predate that — they were imported from Notion and are link collections.
Leave them in their own style; when adding to one, match what is already there.

## Adding to the Wiki

`bin/wiki-add` turns a source into wiki notes: it gets the content, asks Claude to plan which notes
it becomes, drafts each one, and applies what you accept. Every model step after the plan runs with
`claude -p --tools ""`, so the source has to be plain text by then.

**Bundles** are how a source with pictures gets in. `bin/bundle.py` downloads a source into
`tmp/bundles/<slug>/` — `post.md` (the text as markdown, with links into `images/`), `images/`,
`meta.json` (title, author, date for the Source line), and `raw.json` for an X post:

- `bundle.py x <url> <dir>` — an X/Twitter post or Article via the FxTwitter API, which reaches X's
  guest endpoints for us; x.com answers unauthenticated fetchers with HTTP 402
- `bundle.py local <path> <dir>` — a page saved by hand, markdown or complete HTML, file or folder
- `bundle.py curl <file> <dir>` — a paywalled page, where `<file>` holds a command copied with dev
  tools' "Copy as cURL". The command is parsed, never executed by a shell: only the flags that
  describe the request survive, and the session headers are replayed to the article's own host and
  nowhere else. Relative image links resolve against the page URL, and `data-src` wins over `src`
  so a lazy-loaded figure downloads the real file rather than its placeholder

`post.md` is written last, so its presence marks a finished bundle — which is what makes a bundle
directory reusable as a cache.

With a bundle in hand, `wiki-add` describes every image once (`claude -p --allowedTools "Read"`) and
folds the descriptions into the source text as figures, so the tool-less steps downstream can weigh
what an image says. A draft keeps a figure by copying its markdown link; at apply time
`helpers.py wire-images` copies those files into the note's `images/` folder and rewrites the links.

**Fallbacks**, when the download fails: paste a curl command with `--curl`, paste the text, or save
the page yourself and point at it with `--from <path>`.

**Dependencies**: `gum`, `claude`, `jq`, `python3` (`yt-dlp` for YouTube sources, `glow` optional
for nicer draft review).

## Git Commit Guidelines

When creating git commits in this repository:
- **DO NOT** add coding agents (including Claude, Claude Code, or any other AI assistants) as
  co-authors
- Use standard commit messages without AI attribution
- Do not append "Generated with [Claude Code]" or similar footers
- Keep commits clean and focused on the actual changes

## Common Commands

```bash
./bin/wiki                              # Interactive menu (requires gum)
./bin/wiki add <url>                    # Fetch a source and file it into the wiki
./bin/wiki add --curl                   # Fetch a paywalled page with your browser's own session
./bin/wiki add --text <url>             # Paste the text yourself, for anything unfetchable
./bin/wiki add --from <path> <url>      # Read a page you saved: markdown or complete HTML

python3 bin/helpers.py index-link <section-page> <note> "<Title>"   # list a note on its section page
python3 bin/bundle.py x <url> tmp/bundles/<slug>                    # download an X post whole
```
