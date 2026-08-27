# HTML Over Markdown as Agent Output Format

**Source:** [Using Claude Code: The Unreasonable Effectiveness of HTML](https://x.com/trq212/status/2052809885763747935) — Thariq (@trq212), 2026. Examples gallery: [thariqs.github.io/html-effectiveness](https://thariqs.github.io/html-effectiveness/)

## Summary

Markdown became the default communication format between agents and humans because it's simple, portable, and editable. But as agents have gotten more capable and produce larger artifacts, markdown's limits show: people don't read 100+ line markdown files, it can't represent rich information well, and it's awkward to share. The author argues for HTML as the default output format for Claude Code — specs, plans, code reviews, reports, prototypes — because it conveys far more information per artifact, is dramatically more readable and shareable, and supports two-way interaction.

The deeper claim: switching to HTML reverses the cognitive surrender pattern. Because you actually read and engage with HTML artifacts, you stay in the loop on what the agent is doing rather than skimming markdown plans and rubber-stamping them.

## Why HTML Beats Markdown

**Information density.** Almost any kind of information Claude can read can be represented efficiently in HTML: tables, CSS-styled designs, SVG illustrations, embedded code, JS-driven interactions, spatial layouts, images. Without these affordances, models do degraded workarounds in markdown — ASCII diagrams, unicode-character color swatches, etc.

**Visual clarity.** Complex plans and specs are easier to navigate when structured with tabs, illustrations, links, and responsive layout. A 100-line markdown plan goes unread; a well-organized HTML plan gets read.

**Ease of sharing.** Browsers don't render markdown natively. Upload an HTML file to S3 and you have a shareable link your colleagues will actually open. The probability someone reads your spec/report/PR writeup goes up significantly.

**Two-way interaction.** HTML can carry sliders, knobs, drag-and-drop, form controls — letting you tweak parameters and then export the result back as a JSON/markdown/prompt blob to paste into Claude Code.

**Data ingestion advantage of Claude Code specifically.** Unlike chat-based Claude or Claude Design, Claude Code can pull context from the filesystem, MCPs (Slack, Linear, etc.), git history, and a connected browser when generating the HTML.

**It's joyful.** A subjective but real benefit: making HTML artifacts feels more involved and invested than reviewing markdown.

## How to Get Started

You don't need a `/html` skill. Just ask Claude to "make an HTML file" or "make an HTML artifact." The skill lives in knowing **what you want the artifact to do** and how you'll use it — not in any reusable command.

## Use Cases

### Specs, planning & exploration

Instead of a single markdown plan, build a web of HTML files: brainstorm options, expand one, sketch mockups and code snippets, then write the implementation plan. Pass all files into a fresh session for implementation, and into the verification agent for review.

Example prompts:

- *"I'm not sure what direction to take the onboarding screen. Generate 6 distinctly different approaches — vary layout, tone, and density — and lay them out as a single HTML file in a grid so I can compare them side by side. Label each with the tradeoff it's making."*
- *"Create a thorough implementation plan in an HTML file. Include mockups, show data flow, and add important code snippets I might want to review. Make it easy to read and digest."*

### Code review & understanding

HTML can render diffs with inline annotations, flowcharts, severity-colored findings, and module diagrams — often more useful than GitHub's default diff view. Attach an HTML code explainer to every PR.

Example prompt:

- *"Help me review this PR by creating an HTML artifact that describes it. I'm not very familiar with the streaming/backpressure logic so focus on that. Render the actual diff with inline margin annotations, color-code findings by severity, and whatever else might be needed to convey the concept well."*

### Design & prototypes

HTML is highly expressive for design even when the target surface is something else (React, Swift, etc.). Use it to sketch designs, prototype interactions, and tune animations with live controls.

Example prompt:

- *"I want to prototype a new checkout button. When clicked, it does a play animation and then turns purple quickly. Create an HTML file with several sliders and options for me to try different versions, and give me a copy button to copy the parameters that worked well."*

### Reports, research & learning

Claude Code synthesizes across Slack, codebase, git history, and the web well. HTML lets the output be a readable long-form document, an interactive explainer, or even a slide deck — with SVG for diagrams.

Example prompt:

- *"I don't understand how our rate limiter actually works. Read the relevant code and produce a single HTML explainer page: a diagram of the token-bucket flow, the 3–4 key code snippets annotated, and a 'gotchas' section at the bottom. Optimize it for someone reading it once."*

### Custom editing interfaces

When text is a clumsy medium for the task (reordering, structured config, picking values), ask Claude to build a **throwaway single-file editor** purpose-built for the data — always ending with an export button that converts the UI state back into JSON, markdown, or a prompt you can paste into Claude Code.

Example prompts:

- *"I need to reprioritize these 30 Linear tickets. Make me an HTML file with each ticket as a draggable card across Now / Next / Later / Cut columns. Pre-sort by your best guess. Add a 'copy as markdown' button that exports the final ordering with a one-line rationale per bucket."*
- *"Here's our feature flag config. Build a form-based editor: group flags by area, show dependencies between them, warn me if I enable a flag whose prerequisite is off. Add a 'copy diff' button that gives me just the changed keys."*
- *"I'm tuning this system prompt. Make a side-by-side editor: editable prompt on the left with the variable slots highlighted, three sample inputs on the right that re-render the filled template live. Add a character/token counter and a copy button."*

Good fits for this pattern: triaging/bucketing items, editing structured config with constraints, tuning prompts with live preview, curating/labeling datasets, annotating documents or diffs, and picking values painful to express in text (colors, easing curves, crop regions, cron schedules, regexes).

## Tradeoffs

- **Tokens.** HTML uses more tokens than markdown, but with the 1MM context window in Opus 4.7 it's not a meaningful constraint, and the higher likelihood of being read pays for it.
- **Generation time.** HTML takes 2–4x longer than markdown to generate. Worth it for artifacts you'll actually use.
- **Version control.** Biggest downside — HTML diffs are noisy and hard to review compared to markdown.
- **Taste / not ugly.** Use a frontend design plugin/skill, or have Claude generate a single design-system HTML file from your codebase that you reference as a style guide for subsequent artifacts.
- **Viewing.** Open locally in a browser (ask Claude to open it for you), or upload to S3 for a shareable link.

## Core Insight

The shift from markdown to HTML isn't really about format — it's about **staying in the loop**. As agents produce larger plans and specs, markdown's readability ceiling means humans stop reading them and start rubber-stamping. HTML's richness, navigability, and interactivity make the artifact engaging enough that you actually review it, share it, and build on it.

This is a concrete antidote to [cognitive surrender](../../ai-engineering/challenges/cognitive-surrender.md) and [comprehension debt](../../ai-engineering/challenges/comprehension-debt.md): if the artifact is good enough to want to read, you keep the comprehension; if it isn't, you don't.
