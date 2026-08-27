# Research, Plan, Implement (RPI)

**Source:** [Context engineering with Dex Horthy](https://www.youtube.com/watch?v=Usufn8IQJgw) - The Pragmatic Engineer, 2026-07-15

**Companion piece:** [Token Harder vs Token Smarter](../token-harder-vs-token-smarter.md)

## Summary

**RPI** (Research → Plan → Implement) is a three-phase workflow Dex Horthy's team introduced in August 2025 for getting coding agents to solve hard problems in complex codebases. Each phase runs in its own context window, and the artifact produced by one phase is the compressed input to the next — it is **intentional compaction** applied to the software development lifecycle.

The framework has since been substantially revised. The original plan documents listed every line of code that would change, which turned out to be **anti-leverage**: reviewing the plan cost as much as reviewing the pull request, so the human spent twice as long reading. The current version replaces line-level plans with a high-level design step, slices work vertically rather than horizontally, and treats all the documents as disposable.

## The Original Three Phases

- **Research** — don't tell the agent what you're building. Ask it how the relevant systems work and how they connect. Fan out sub-agents in parallel across the codebase. Burns ~100k tokens of context, emits a ~10k token markdown doc.
- **Plan** — new context window, seeded with the research doc. "Here's what we're building, here's the research, build a plan."
- **Implement** — new context window again, seeded with the plan.

The compaction is the point: each step reads a lot and writes a little, so the next step starts near the top of the [smart zone](../token-harder-vs-token-smarter.md) rather than inheriting a bloated trajectory.

**Why planning caught on in mid-2025:** Horthy's retrospective read is that plans were a powerful lever for getting agents to *work for longer*. "Build me a B2B SaaS for burrito delivery" got you a homepage. "Build me a plan," then "here's the plan, go implement it," got the agent to keep going until the plan was done. The plan anchored the agent and reminded it that it wasn't finished.

## What Was Wrong: Anti-Leverage

The original plan doc spelled out every changed line — diff blocks, all the new code to write. The team recommended reading these plans, and did read their own. Then:

- Horthy noticed he had started **skimming** them, so the plan stopped functioning as a re-steering point.
- Teams that did read them carefully ended up reviewing twice: 20 minutes on the plan, 20 minutes on the PR, and the two documents are *different*.
- Net effect: **you doubled the time spent reading code instead of reducing it.** That's anti-leverage — effort added at a checkpoint that doesn't reduce effort downstream.

The correct test for any checkpoint: does an hour spent here save more than an hour later? Horthy's target is an hour of planning that turns a six-hour PR review into a twenty-minute one.

## The Revised Shape: Research → Design → Plan → Implement

Each phase exists because models have a *specific* shortcoming at that stage:

- **Research is hands-off.** Horthy doesn't read the research docs. Asking a model "what is the intent and how does this fit together" is something models are "pretty damn good at." (Asking it to find a bug or have opinions is a different, harder task.)
- **Design needs a human.** A design doc covers current state, desired end state, and a set of design questions — an over-engineered plan mode. Models make architecture and program-design decisions that are sometimes right and sometimes wrong, so this is where human taste belongs.
- **Plan needs correcting for horizontal slicing** (below).
- **Implement** runs against research + design + plan, all compressed.

## Vertical vs Horizontal Plan Slicing

Left alone, models produce **horizontal plans** — layer by layer:

> database → services layer → API → frontend

This is bad because you end up on the far side of 2,000 lines of code in an existing system with nothing testable until the very end.

A human building by hand slices **vertically** instead:

1. Mock API endpoint with fake data
2. Get the frontend roughly how you want it to look
3. Build the services layer, wire real data through
4. Database migration, new table
5. Business logic
6. Error handling

Horthy's framing: "I would rather read five separate little mini diffs of things that I can manually verify and explore than read 2,000 lines of code and be like, well, it's not working. I don't know where." With a horizontal plan the model writes the database layer and all the error handling before anyone has seen the code run.

This is the same instinct that shows up in [Harness Engineering](../harness-engineering.md) — shaping the environment and the work so every turn of the agent produces something verifiable.

## Why the Docs Are Throwaway

RPI docs are **tactical execution docs**, not evergreen artifacts. Research, plan, implement, then throw the docs out. Next task, redo the research from scratch.

The reasoning:

- **Tokens are cheap, your time is expensive.** Regenerating research costs a few dollars.
- **Stale research is worse than no research.** The time you waste acting on a doc that no longer matches the codebase exceeds what you saved by reusing it.

This is also Horthy's answer to spec-driven development. He's been on a spec-kit GitHub issue open for a year where people keep arriving with the same complaint: *I edit my specs, then I edit the code, the code drifts, how do I keep the specs current?* You now have **two sources of truth**, and it stops being useful.

- The OpenAI-researcher version of spec-driven dev — stop reading code, write specs, treat coding as compiling specs into code — "never really materialized."
- Horthy has seen people maintain parity between docs/specs and code. It works, and it's probably automatable with AI. But: "I've never known anyone who was like, yeah, this is great and we're glad we have it."
- Default position: **the code is the source of truth, always.**

Note the terminology muddle he flags — for many people "spec-driven development" now just means "I use a bunch of markdown files while coding," and some people call RPI spec-driven dev for that reason.

## Core Insight

**Plans are only worth writing at a level of abstraction where reviewing them is cheaper than reviewing the code.** A plan that enumerates every changed line is just the diff with extra steps — you pay the review cost twice and gain nothing. The leverage lives one level up: compress the codebase into research, compress intent into a design the human actually argues with, then slice the work vertically so every step produces something you can run.

And the artifacts are scaffolding, not documentation. The moment a doc has to be *kept in sync* with the code, it has become a second source of truth and a liability — regenerate it on demand instead.
