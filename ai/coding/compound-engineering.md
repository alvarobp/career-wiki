# Compound Engineering

**Source:** [Compound Engineering Guide](https://every.to/guides/compound-engineering) - Kieran Klaassen (Every), 2026
**See also:** [Compound Engineering: The Next Paradigm Shift](https://www.vincirufus.com/posts/compound-engineering/) - Vinci Rufus, January 2026

## Summary

Compound engineering is a framing where each unit of engineering work makes subsequent units easier — not harder. Traditional development tends to accumulate complexity over time. Compound engineering tries to invert that: features teach systems new capabilities, bug fixes eliminate future bug categories, and codified patterns become reusable tools. The argument is that the jump from "vibe coding" (30-70% productivity gains) to much larger gains comes not from faster code generation, but from tighter feedback loops, better specifications, and systematic knowledge capture.

## The Main Loop: Plan → Work → Review → Compound

The core cycle has four phases:

1. **Plan** — Turn ideas into blueprints: understand requirements, research codebase patterns, design solutions. The authors argue this is where the most human value lives.
2. **Work** — Agent-driven execution with continuous validation (tests, linting, type checking) running throughout.
3. **Review** — Analysis catching issues and capturing learnings across security, performance, architecture, and quality.
4. **Compound** — Capture reusable insights, update instructions and agents, verify the system catches similar issues automatically next time. The authors note this is the phase most teams skip — and why they plateau.

The suggested time split is 80% planning/review, 20% working/compounding.

## The Productivity Equation

> Productivity = Code Velocity × Feedback Quality × Iteration Frequency

The key insight: when code generation approaches instant (via AI), feedback loops become the real bottleneck. If generation takes 30 seconds but validation requires 2 hours, velocity is capped at feedback speed. The compression targets:

- **Code generation:** hours → seconds
- **Validation:** manual → automated
- **Testing:** pre-deployment → continuous
- **Deployment:** manual steps → automated pipelines

## Mindset Shifts

The authors identify several assumptions worth questioning:

- **"Code must be hand-written"** — Quality matters; authorship may not
- **"Every line needs manual review"** — Automated systems can catch the same issues
- **"Code is the primary artifact"** — The systems producing code may matter more than individual implementations
- **"First attempts should be good"** — High garbage rate on first pass is expected; the advantage comes from iterating fast
- **"Typing equals learning"** — Reviewing many implementations can teach more than hand-writing a few

And some ideas they propose in their place:

- **Extract taste into systems** — Encode preferences in agent instructions and tooling rather than relying on code review to transfer knowledge
- **The 50/50 rule** — Spend roughly half of engineering time on system improvement (pattern documentation, test generators, automated reviewers) rather than only shipping features
- **Trust through safety nets** — Trustworthiness comes from verification infrastructure (tests, monitoring, automated review), not from manual gatekeeping
- **Plans as primary artifacts** — Plans document decisions before they become bugs; they capture intent and enable review at the right abstraction level
- **Parallelization as strategy** — When compute replaces human attention as the bottleneck, running agents and features in parallel becomes a natural lever

## Guardrails

As generation speed increases, imprecise instructions create costly iteration cycles. Some guardrail approaches mentioned:

- **Specification as code** — Executable requirements rather than prose documentation
- **Type constraints** — Strong typing that narrows the space of valid solutions
- **Prompt templates** — Project-contextualized frameworks with architectural patterns baked in
- **Verification-first** — Giving the AI a way to verify its own work through integrated test execution

## Useful Questions for AI Output

Three questions the authors suggest for evaluating any AI-generated work:

1. **"What was the hardest decision?"** — Surfaces judgment calls
2. **"What alternatives did you reject, and why?"** — Shows the option space considered
3. **"What are you least confident about?"** — Identifies weak spots

## Core Principles

- Every unit of work should compound into the next
- Taste belongs in systems, not in reviews
- Teach systems rather than doing the work yourself
- Safety nets over gatekeeping
- Structure projects for agent autonomy
- Measure output by problems solved, not keystrokes

## Connections to Other Concepts

- **Write-only code** — Compound engineering provides the verification infrastructure needed when humans stop reading every line of AI-generated code
- **Backpressure for agents** — Feedback loops and guardrails are a form of backpressure, keeping agents from running ahead of the system's ability to validate
- **Context engineering** — The compound phase builds the context (instructions, solutions, patterns) that makes future agent work more effective
