# Intent Debt: The Missing *Why* Behind the Code

**Source:** [Intent Debt](https://addyosmani.com/blog/intent-debt/) — Addy Osmani, June 5, 2026

**Companion piece:** [Comprehension Debt](./comprehension-debt.md) — same author; maps to *cognitive debt* in the triple-debt model below. See also [Cognitive Surrender](./cognitive-surrender.md).

## Summary

**Intent debt is the absence or erosion of the externalized rationale, goals, and constraints that explain *why* a system is the way it is.** It is distinct from messy code (technical debt) and from not understanding the code that exists (cognitive debt). Intent debt is about the reasoning behind decisions living only in people's heads — never written down — so it cannot be recovered by reading the system itself.

The problem becomes acute with AI agents because **an agent can't generate intent — intent is the one input that has to come from you.** An agent can refactor code, explain what code does, and even infer structure, but it cannot reconstruct the *why* behind a design choice that was never recorded. With agents running constantly, the cost of missing intent is no longer paid once in a hallway conversation — it's paid every session, multiplied by every agent you run.

## The Triple Debt Model

Osmani draws on Margaret-Anne Storey's framework, which separates three *independent* forms of software debt:

| Debt | What's missing | Recoverable from code? |
|---|---|---|
| **Technical debt** | Good implementation — poor choices hinder future change | Yes (you can read the bad code) |
| **Cognitive debt** | Human understanding of the system's complexity | Partially (re-reading rebuilds it) |
| **Intent debt** | The externalized *why* — goals, constraints, rationale | **No** — if never written, it's gone |

The three are independent: clean, well-understood code can still carry heavy intent debt if nobody recorded *why* it was built that way.

## Why Intent Debt Is Uniquely an Agent Problem

- Agents are excellent at the things code *does* contain: structure, behavior, patterns.
- Agents are helpless at the thing code *doesn't* contain: the reasoning that produced it.
- Pre-agent, intent survived informally — institutional memory, the person who "just knows," a quick Slack thread. That channel doesn't exist for an agent starting cold.
- Every fresh agent session re-pays the cost of unexplained decisions. The economics flip from "occasionally re-derive intent" to "re-derive intent constantly, in parallel."

## How High Intent Debt Manifests

- An agent **removes a guard or workaround** because nothing recorded why it was there.
- A refactor **changes undocumented, user-dependent behavior** that was load-bearing but unexplained.
- An agent makes a design choice with **no recorded rationale**, adding *new* intent debt on top of the old.

The failure mode is silent: the code still compiles and the tests still pass, because the lost information was never expressed as code or test in the first place.

## Mitigations: Externalize the Intent

The fix is to move intent out of heads and into durable artifacts the agent reads every session:

- **Specifications** — capture goals, constraints, and the definition of "done" before building.
- **Intent ledgers** — `AGENTS.md` (and similar) files documenting conventions, constraints, and the reasoning behind them, loaded into every agent's context.
- **Decision logs (ADRs)** — record the rationale *at the moment of the decision*, when the why is still fresh, not reconstructed later.
- **Learning loops** — have agents document why an approach succeeded or failed, so hard-won reasoning is captured rather than re-discovered.

## Core Insight

> Write down the *why*, because it's becoming the most valuable thing you can leave in the repo.

Code, structure, and even understanding can be regenerated or rebuilt from what's already there. Intent cannot — it is the one input only a human can supply, and the only debt an agent can neither detect nor repay. As agents do more of the building, the scarce, durable, human contribution shifts from writing code to recording the reasoning that makes the code legible to everyone — and everything — that touches it next.
