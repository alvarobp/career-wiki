---
name: wiki-add
description: >
  Incorporate knowledge from URLs, text, images, or any context into this career wiki.
  Use when the user provides a URL, article, text snippet, image, or any piece of knowledge they
  want to capture in the repository. Triggers on: "incorporate this", "add this to the wiki",
  "save this article", sharing a URL with intent to document it, or any request to extract and
  store knowledge from given context. Also triggers when the user says "/wiki:add" or
  provides content with guidance on where to store it.
---

# Add to the Wiki

Extract knowledge from any provided context (URLs, text, images, files) and incorporate it into
this wiki as a well-structured markdown note.

## How this wiki is laid out

The repository root *is* the wiki, and it is an Obsidian vault. Everything at the top level is a
section except `bin/`, `.claude/`, `tmp/` and `README.md`.

- **On disk, everything is kebab-case ASCII**: `ai/context-engineering.md`.
- **In the text, titles keep their natural capitalisation**: the note's real title is the H1 on its
  first line, and link labels are written that way too —
  `[Context Engineering](context-engineering.md)`.
- **A section is a folder, and its own page is the note inside it that shares its name.**
  `architecture/` is a section; `architecture/architecture.md` is its page. That page carries the
  list of links to everything in the section — that list is how the vault is navigated.
- **A plain note is a file in its section's folder.** A note that grows sub-notes of its own becomes
  a folder of its own name, with its content moving to `<name>/<name>.md`.
- **Images live in an `images/` folder** beside the note that uses them; other attachments (PDFs,
  archives) live in `attachments/`.
- **`README.md` at the root** lists the top-level sections and nothing else.

Never put a new note at the root: every note belongs to a section.

## Workflow

### 1. Gather the knowledge

Accept any form of input:
- **URLs**: Fetch and extract content using WebFetch
- **X/Twitter posts and Articles**: WebFetch gets HTTP 402 from x.com. Download the post instead:
  `python3 bin/bundle.py x <url> tmp/bundles/<slug>`. That writes `post.md` (the text as markdown)
  and `images/` (every picture in it). Read the images — in an Article of annotated slides they
  carry as much as the words do.
- **A page saved by hand**: `python3 bin/bundle.py local <path> tmp/bundles/<slug>` takes markdown
  or complete HTML, a file or the folder a browser saved it into, and produces the same shape.
- **YouTube videos**: `bin/download-youtube-transcript.sh <url> tmp/transcript.txt` pulls the
  captions; the watch page itself has nothing fetchable on it.
- **Text/quotes**: Use directly as provided
- **Images**: Read and extract key information
- **Multiple sources**: Process each and synthesize

When the source came with images, keep one in the note only if the image itself carries the idea — a
diagram, a chart, a table the words cannot replace. Copy the file into an `images/` folder beside
the note and link it relatively, the way
`ai/agentic-systems/master-ai-agentic-engineering/workflow-design-patterns/`
does. Title cards and decorative shots never earn a place.

### 2. Determine what to incorporate

**If the user provides guidance** on what to extract or focus on, follow that direction.

**If no guidance is given**, analyze the content and propose:
- What key insights, principles, or knowledge to capture
- Which section it belongs to
- A suggested title, and the kebab-case filename that follows from it

Present the proposal to the user before writing.

### 2b. Decide how many notes the source becomes

One source is not always one note. Classify it into one of four shapes:

| Shape | What to produce |
|---|---|
| **Single topic** | One note. |
| **Several aspects of one topic** | Still one note; the aspects become sections. Don't over-split. |
| **Several distinct topics** | A **hub** note summarizing the source, plus one **spoke** note per topic, cross-linked. |
| **Already covered** | **Merge** into the existing note instead of creating a near-duplicate. |

Two rules keep this from fragmenting or bloating the wiki:

- **Split test** — give a topic its own note only if it is *independently referenceable*: someone
  who never saw this source would search for it by name and expect a standalone note. Otherwise it
  stays a section.
- **Merge test** — merge only when the source adds a distinct claim, contradicts the note, or
  supplies new evidence. "Related to the topic" is not enough; a merge that only adds a citation
  makes the note longer without making it say more.

A source can also produce a mix: two new notes plus an edit to an existing one. Propose the whole
plan — new notes, merges, and links to add — and confirm it before drafting anything.

A hub whose spokes are numerous enough to crowd its section becomes a folder: the hub moves to
`<hub>/<hub>.md` and the spokes sit beside it. That is what
`ai/coding/agentic-engineer-principled-ai-coding/` is.

### 3. Choose the right section

Top-level sections:

| Section | Purpose |
|---|---|
| `agile/` | Agile practice: XP, CI/CD, trunk-based development, pairing |
| `architecture/` | Software architecture, microservices, serverless, cloud native |
| `ai/` | AI engineering, agentic systems, prompt and context engineering |
| `development/` | Day-to-day development practice, design principles, technical debt |
| `devops/` | Observability, incident management, monorepos, environments |
| `frontend/` | Frontend development and testing |
| `gis/` | Geospatial |
| `infrastructure/` | Kubernetes, infrastructure as code |
| `jobs/` | Companies, hiring, applications |
| `management/` | Engineering management, career paths |
| `organisation/` | Culture, teams, autonomy, consensus, change |
| `product/` | Product management, discovery, ownership |
| `programming-languages/` | Language-specific material |
| `quality-assurance-testing/` | Testing strategy, TDD, test design |
| `resources/` | Books, courses, newsletters |
| `self-organization-productivity/` | Personal productivity |
| `soft-skills/` | Communication, feedback |
| `sre-operations/` | Reliability and operations |

If none of these fit well, suggest creating a new section. Prefer using existing sections when the
content reasonably fits.

**Categorize every note independently**, on what *that note* is about — not on where its siblings
went. Notes from one source routinely land in different sections.

When a single note genuinely straddles two sections, never write it twice: two copies diverge the
moment one is edited. Pick its primary home by its subject, and cross-link it from the neighbouring
note.

### 4. Write the note

New notes follow this format, whatever the older imported notes around them look like:

```markdown
# Title

**Source:** [Title](url) - Author, Date
<!-- or: **Source:** Description of where this came from -->

## Summary

A concise 1-2 paragraph summary of the core idea.

## Section Headings for Key Concepts

Break down the main ideas into logical sections. Use clear headings.
Include bullet points for specific details, examples, or lists.

## Core Insight (or Practical Implications, Takeaways, etc.)

The distilled essence — what makes this knowledge worth keeping.
```

Guidelines:
- Keep it concise and high-signal — only capture what's worth referencing later
- Use the author's framing and terminology where valuable
- Structure for scanability: headings, bullets, bold key terms
- Attribute the source clearly at the top
- Filename: `<section>/kebab-case-name.md`, where the name is the kebab-case form of the H1

Cross-linking:
- A **hub** ends with a `## Related notes` section linking every spoke with a one-line description
- A **spoke** carries a `**Companion piece:**` line just under the Source line pointing at the hub
- Links are relative paths between notes: `./sibling.md`, `../other-section/sibling.md`

Adding a backlink into an *existing* note is the easiest thing to overdo, so hold it to the same
bar as a merge: only when a reader of that note is materially under-served without the pointer.
Sharing a general subject is not enough. Three is a lot.

When a note draws on more than one source, replace the single `**Source:**` line with a
`**Sources:**` list naming each.

### 4b. List the note on its section's page

A note nothing links to is a note nobody finds. After writing a new note, add it to the list on its
section's page (`<section>/<section>.md`), in the same bare-link style that page already uses:

```markdown
[Context Rot](context-rot.md)
```

`python3 bin/helpers.py index-link <section-page> <note> "<Title>"` does this and is a no-op if the
link is already there. A brand-new section needs its own page too — `<section>/<section>.md` with
the section title as its H1 — and that page listed in the parent section's page or in `README.md`.

### 4c. Merge into an existing note

When the plan calls for a merge, make a **scoped edit** — insert the new material at the right
place and leave everything else byte-for-byte alone. Never regenerate the note.

- Match the note's existing voice, heading style, and level of detail
- Attribute the new material to its source inline, since the note was written from a different one
- Update the header to the `**Sources:**` list form if this is the note's second source

Most notes here were imported from Notion and are link collections rather than prose. Merging into
one of those means adding a link or a short block in the style already there — not rewriting it into
the format above.

### 5. Confirm with the user

After writing, list every file created and every file edited, each with a one-line summary of what
landed there, and say which section pages were updated. When the source produced a hub and spokes,
say which note is the hub.

## The scripted path

`bin/wiki-add <url>` runs this whole workflow non-interactively with a review step at each stage —
bundle the source, describe its images, plan the notes, steer the plan, draft, review each draft,
apply. Prefer it when the user just hands over a URL; work through this skill by hand when the
source is something the script cannot fetch, or when the user wants to discuss as you go.
