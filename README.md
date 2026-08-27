# Career Wiki

Everything worth keeping about software engineering practice — notes, references and material
collected over a career. The repository root is the wiki itself, kept as a plain-markdown
[Obsidian](https://obsidian.md) vault.

## Sections

[AI](ai/ai.md)

[Infrastructure](infrastructure/infrastructure.md)

[Architecture](architecture/architecture.md)

[Organisation](organisation/organisation.md)

[Product](product/product.md)

[Agile](agile/agile.md)

[Quality Assurance & Testing](quality-assurance-testing/quality-assurance-testing.md)

[Programming Languages](programming-languages/programming-languages.md)

[Development](development/development.md)

[Management](management/management.md)

[Soft Skills](soft-skills/soft-skills.md)

[DevOps](devops/devops.md)

[GIS](gis/gis.md)

[Frontend](frontend/frontend.md)

[Resources](resources/resources.md)

[Tooling](tooling.md)

[Project Management](project-management.md)

[Self-Organization / Productivity](self-organization-productivity/self-organization-productivity.md)

[Jobs](jobs/jobs.md)

[SRE / Operations](sre-operations/sre-operations.md)

## Adding to the wiki

`bin/wiki` turns a source into wiki notes: it gets the content, plans which notes it should become,
drafts each one, and applies what you accept.

```bash
wiki                              # interactive menu
wiki add <url>                    # fetch a source and file it into the wiki
wiki add --curl                   # fetch a paywalled page with your browser's own session
wiki add --text <url>             # paste the text yourself, for anything unfetchable
wiki add --from <path> <url>      # read a page you saved: markdown or complete HTML
```

X posts, X Articles and YouTube videos are downloaded whole, images and captions included; other
URLs are fetched. When a fetch fails you are offered the other routes instead.

### Paywalled articles

An article you are subscribed to is readable in your browser and nowhere else — the session lives in
that browser's cookies. `wiki add --curl` borrows it: in dev tools, **Network → reload →
right-click the document request → Copy → Copy as cURL**, then paste the command when asked. The
page is fetched exactly as the browser saw it, images included, and the URL comes from the command
so you needn't give it separately.

Nothing in the paste reaches a shell. The command is parsed, and only the flags that describe the
request — headers, cookies, method, body — are honoured; anything else is dropped. Your session
headers are replayed to the article's own host and to no other, so an image on a third-party CDN is
fetched anonymously.

### Installation

Alias the entry point in your shell configuration:

```bash
alias wiki='~/personal/code/career-wiki/bin/wiki'
source ~/personal/code/career-wiki/bin/bash-completion.sh   # optional tab completion
```

**Requirements:** [gum](https://github.com/charmbracelet/gum), the `claude` CLI, `jq` and `python3`.
`yt-dlp` is needed for YouTube sources and [glow](https://github.com/charmbracelet/glow) renders
drafts more readably during review.

Inside a Claude Code session the same workflow is available as `/wiki:add <url>`, or by just handing
over a URL — the `wiki-add` skill in `.claude/skills/` picks it up.

## Conventions

Filenames and folders are kebab-case; titles keep their natural capitalisation in the note's H1 and
in link labels. A section is a folder whose own page is the note inside it that shares its name, and
that page lists everything in the section. See [CLAUDE.md](CLAUDE.md) for the full set.
