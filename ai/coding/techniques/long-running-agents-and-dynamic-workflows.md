# Long-Running Agents and Dynamic Workflows

**Source:** [Boris Cherny: Stop Hobbling Your AI](https://www.youtube.com/watch?v=qyPCVqFUyDo) - Y Combinator, 2026-07-27

## Summary

The headline capability of the current model generation is duration: agents that run productively for days or weeks without stopping. Boris Cherny's claim is that this requires almost no scaffolding — no `/goal`, no `/loop`, no clever prompt. What it requires is a task that is slightly **too hard**, and a way for the model to **verify its own work** so it never gets stuck. Verification is, in his words, "the single most important thing that people do not get right."

On top of that base, Claude Code exposes **dynamic workflows** — an algebra for running agents in sequence and in parallel inside a sandbox — which Cherny frames as a genuinely new axis of test-time compute. Paired with **loops and routines** (scheduled, repeating agent runs), the same machinery is now used at Anthropic to automatically maintain the codebases of the CLI, desktop, iOS, and Android apps.

## The Recipe for a Multi-Week Task

The pattern is deliberately unglamorous:

- **Give a task slightly harder than you think the model can do.** Over-specification is the common failure mode — "do this, then this, then this" is how you built systems in the past, not how you drive modern models.
- **Describe the task, the guardrails, and the exit criteria** at a high level, then let the model cook and come back later.
- **Give it a verification loop.** Without one it gets stuck or hallucinates its way to "done"; with one it self-corrects indefinitely.
- **Steering is allowed.** These runs are not one-shot — Cherny is explicit that the Bun rewrite involved steering. What changed is that previous models couldn't do it *even with* steering.

### Two worked examples

- **Bun: Zig → Rust.** The Bun team had been using Claude to fuzz for memory leaks one case at a time. Jared on the team instead threw the whole rewrite at it as a test problem each model generation; starting with Fable it worked. One prompt, a dynamic workflow, **11 days**, a 100k+ line JavaScript runtime rewritten — now in production, and what Claude Code runs on. Prior human estimate: well over a year. The enabling detail is that **Bun and Node.js both have large test suites**, so correctness was cheap to check.
- **Claude desktop: Electron → Swift.** Cherny's entire prompt, issued from Claude in Slack: rewrite the Electron app in Swift, run the Electron app in a macOS VM, screenshot it, compare **pixel by pixel** against the Swift version, and don't stop until done. He first had to hand it a macOS GitHub runner and repo access — it correctly reported "no" when it lacked them. At the time of the talk it had been running **~14–15 days and was still going**, and had spontaneously created a Slack channel to live-blog screenshots of its own progress.

Both examples share the same shape: a mechanical oracle for correctness (test suite, pixel diff) plus a task large enough that the model has to sustain itself.

## Dynamic Workflows as an Algebra for Agents

To trigger one in Claude Code, you say: **"use a workflow."** That's the whole interface.

- Claude Code uses the **Bun runtime as a sandbox**, starting a VM inside it and letting Claude spawn and orchestrate agents there.
- It is not one agent, nor a flat fan-out of ten parallel agents. A workflow **stages** itself: a first pass fans out agents; a second stage has a different set verify or summarize that work; a third stage fans out again.
- The design draws on Cherny's functional programming background: **agents in sequence, agents in parallel**, with tools to compose them and keep token use efficient.
- Suited to work like rewriting a codebase, deep analysis over complicated data, or a multi-stage feature spanning dozens of pull requests.

**Why this matters conceptually:** scaling has historically been a function of neural net size, training data, and training flops; then test-time compute (how many tokens the model generates) was added. Dynamic workflows are framed as **a new way to orchestrate test-time compute** — a lever for dramatically increasing the compute spent on one hard task. Cherny notes this is a genuinely new form that "hasn't really been written about a lot." Realistic scale for a single long-running task: **thousands to tens of thousands of agents**.

## Loops and Routines: Self-Maintaining Codebases

A different shape of long-running work:

- **Loop** = a cron job running locally for Claude. **Routine** = the same thing running in the cloud, so you can close your laptop.
- The distinction from dynamic workflows: a workflow is **one task broken into chunks**; a loop/routine is **one repetitive task** that does *not* share context between runs but *may* share memory. Cadence can be hourly, every five minutes, or daily.

Anthropic now runs **20–30 routines daily across the CLI, iOS, Android, and desktop codebases** — hundreds to thousands of agents a day, doing what used to take dozens or hundreds of engineers. Each is roughly a one-sentence prompt:

- **Clean up dead code** — finds it across all codebases using static *and* dynamic analysis (nobody prompted the dynamic analysis; it figured that out), and opens a PR daily.
- **Ship finished experiments** — an experiment already at 100% gets its flag deleted from the codebase and shipped.
- **Write tests** for areas lacking coverage.
- **Delete tests** that shouldn't exist — useless ones added by older models or by people at some point.
- **"Abstraction police"** — finds near-duplicate abstractions that drifted apart across a large codebase and unifies them.

The stated destination is fully automated maintenance of their apps, freeing engineers to ship new product and talk to users.

## Core Insight

**Duration is unlocked by verification, not by scaffolding.** The instinct is to reach for orchestration features, elaborate prompts, and step-by-step specification; the actual constraint is whether the model has a mechanical way to check itself. Given a test suite or a pixel diff, an over-ambitious task becomes a stable multi-week loop — this is the concrete face of [Product Overhang and Unhobbling](../../ai-engineering/principles/product-overhang-and-unhobbling.md), where the capability already existed and only the harness was in the way.

Two structural consequences worth internalizing:

- **Test-time compute now has an orchestration axis.** How much thinking you can throw at a problem is no longer bounded by one context window's token budget but by how well you can compose agents in sequence and parallel. Investing in verifiability is therefore investing in scale.
- **Codebase maintenance is becoming a background process.** Dead code, test hygiene, flag cleanup, and abstraction drift — the work that always loses to feature pressure — fits the loop/routine shape almost perfectly, since each run is repetitive, independently verifiable, and needs no shared context.

The complementary discipline is knowing what to delete from the harness in the first place, covered in [Ablation-Driven Harness Design](./ablation-driven-harness-design.md).
