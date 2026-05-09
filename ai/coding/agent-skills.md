# Agent Skills: Encoding Senior Engineering Discipline into AI Agents

**Source:** [Agent Skills](https://addyosmani.com/blog/agent-skills) — Addy Osmani, May 2026

**Companion pieces:** [Comprehension Debt](../ai-engineering/challenges/comprehension-debt.md) and [Cognitive Surrender](../ai-engineering/challenges/cognitive-surrender.md) — same author. Where those articles diagnose what AI coding loses, Agent Skills proposes the operational fix: encode the lost discipline as workflows the agent must follow.

## Summary

AI coding agents default to the **shortest path to completion**, skipping the invisible work that distinguishes reliable engineering from code that breaks. Agent Skills is a framework that enforces senior-engineer practices by encoding them as **executable workflows rather than reference documentation**.

A skill is a markdown file with frontmatter that injects a structured workflow into the agent's context: "a sequence of steps the agent follows, with checkpoints that produce evidence, ending in a defined exit criterion." The critical distinction is that skills are **executable processes, not essays** — they describe what to *do*, in what order, with what proof of completion.

## The Six Lifecycle Phases

Skills organize around standard SDLC phases, each invoked as a slash command:

1. **Define** (`/spec`) — Establish what you're building
2. **Plan** (`/plan`) — Break work into manageable pieces
3. **Build** (`/build`) — Implement in vertical slices
4. **Verify** (`/test`) — Prove correctness
5. **Review** (`/review`) — Catch oversights
6. **Ship** (`/ship`) — Deploy safely

Plus `/code-simplify` as a cross-cutting concern.

## Five Load-Bearing Design Principles

**1. Process over prose.** Workflows are agent-actionable; essays are not. The same applies to human teams under time pressure — a checklist with checkpoints survives contact with a deadline; a paragraph of guidance does not.

**2. Anti-rationalization tables.** Each skill pairs common excuses with written rebuttals. Example: *"This task is too simple to need a spec"* is countered by *"Acceptance criteria still apply. Five lines is fine. Zero lines is not."* This pattern preempts plausible-sounding justifications for skipping rigor — the lies a team tells itself are documented and refuted in advance.

**3. Verification is non-negotiable.** Every workflow terminates in concrete evidence: test passes, clean build output, reviewer sign-off. **"Seems right" is insufficient.** No skill exits without a checkable artifact.

**4. Progressive disclosure.** Load only the relevant skills into context based on the current phase. Prevents context degradation from unused content — the agent isn't carrying the review checklist while it's still planning.

**5. Scope discipline.** Touch only what was explicitly requested. Prevents the scope creep that makes PRs unmergeable and makes large changes invisible to reviewers.

## Integration with Established Engineering Practices

The skills bake in practices documented in *Software Engineering at Google* and the broader engineering canon:

- **Hyrum's Law** (API design): Observable behavior becomes depended-upon behavior
- **Test pyramid + Beyoncé Rule**: Test code should read as specification
- **DAMP over DRY in tests**: Avoid over-abstraction in test code
- **~100-line PRs with severity labels**: Large PRs don't get reviewed
- **Chesterton's Fence** (simplification): Understand why something exists before removing it
- **Trunk-based development and atomic commits**
- **Shift Left + feature flags**: Detect problems early, not in production
- **Code-as-liability**: Minimize surface area to maintain

The skills aren't novel principles — they're a delivery mechanism that forces the agent to actually apply principles humans already agree are correct.

## Tool-Agnostic Patterns to Steal

Whether or not you adopt the framework directly, these patterns transfer to any agent setup:

1. **Document team rationalizations and write rebuttals** — capture the lies you tell yourselves about when rigor doesn't apply
2. **Convert reference documentation to workflows with checkpoints** — prose-shaped knowledge is invisible to agents under pressure
3. **Make verification the mandatory exit criterion** for every task
4. **Use routers instead of massive handbooks** — load skills on demand by phase
5. **Adopt five non-negotiables**: surface assumptions, resolve conflicts, push back when warranted, prefer boring solutions, respect scope boundaries

## Position in Broader Agent Architecture

Skills are one layer of agent harness engineering, sitting alongside:

- **`AGENTS.md`** — rolling rulebook, always-on context
- **Hooks** — deterministic enforcement at tool-call boundaries
- **Tools** — the available actions
- **Session logs** — durable memory across runs
- **Skills** — phase-scoped workflows with verification

They matter most for **long-running agents**, where skipped steps compound into archaeological debugging problems weeks later.

## Installation Modes

1. Install via Claude Code marketplace for automatic activation
2. Drop the markdown into tool-specific rule directories (Cursor, Gemini CLI, etc.)
3. Use the skills as a *specification* for your team's own engineering practices — independent of any tool

## Core Insight

> The senior-engineer parts of work are no longer optional, even when the engineer is a model.

The framework reframes AI agents as **extremely able junior engineers lacking instinct for invisible work**. The job becomes encoding discipline so rigorously that the agent cannot rationalize shortcuts. Capability isn't the bottleneck; the bottleneck is whether the harness around the agent makes the right behavior the path of least resistance.

This connects directly to the [comprehension debt](../ai-engineering/challenges/comprehension-debt.md) problem: skills are how you keep verification, scope, and review from being silently dropped at the moment generation speed makes them feel like overhead.
