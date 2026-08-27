# Product Overhang and Unhobbling

**Source:** [Boris Cherny: Stop Hobbling Your AI](https://www.youtube.com/watch?v=qyPCVqFUyDo) - Y Combinator, 2026-07-27

## Summary

Boris Cherny, creator of Claude Code, frames the central opportunity in AI product building as a gap between what models can already do and what products let them do. **Product overhang** is the set of capabilities today's models possess that no product has yet elicited. **Hobbling** is the flip side: scaffolding, over-specification, and product design that actively get in the model's way. The two are "two sides of the same thing."

The practical claim is that you don't need to wait for a better model to build something new. At every model generation there is a large, unclaimed set of behaviours — new tools, new languages, new problem classes, new ways of working — that the model can express but no product invites it to. Finding one of those is how new categories get born.

## The Origin Story of Claude Code

Cherny uses Claude Code itself as the canonical example of closing an overhang:

- The model was **Sonnet 3.5**, roughly 18 months to 2 years before the talk — the best coding model of its time, "a pretty terrible coding model by modern standards."
- The products of that era offered **single-line autocomplete**, sometimes multi-line autocomplete, and **read-only chat** about a codebase.
- Nobody had built a product eliciting the model's actual capability: writing **entire functions and entire files** at a time.
- The design move was subtractive — "get rid of all the scaffolding and just give the model the simplest possible harness."

The insight: the model was already capable, and every existing product was getting in the way. IDE-shaped rigidity was the hobbling; full terminal access was the unhobbling.

## How to Find an Overhang

**Give the model slightly harder tasks than you think it can do.**

- The most common failure mode Cherny sees is over-specific instruction: "I want you to do this, but do it this way, this way, this way. You must do one, then two, then three, then four."
- For modern models this is the wrong shape. Instead: describe **the task**, describe **the guardrails**, describe **the exit criteria**, and "let the model cook."
- Keep throwing the latest model at an unsolved practical problem — a business, engineering, or product problem. Even if the previous model failed, the new one might not.

**Experiment without a commercial thesis.**

- An internally viral discovery at Anthropic: give Opus 5 **OpenCV** and ask it to draw. It produces credible portraits, animals, landscapes.
- The model was never trained to draw. "It's just the elicitation gap — if you ask it to do it the right way, it can just do it."
- This was found by "playing around and trying creative things that didn't have direct commercial applications."
- Cherny's hypothesis: **dozens or hundreds** of comparable opportunities exist in today's models that nobody has realised yet.

## Verification Is the Bottleneck, Not Prompting

The skill has shifted away from prompt engineering (and its successor fashion, context engineering). What matters now:

1. How do you give Claude a task that seems **a little too hard**?
2. How do you make it possible for Claude to **verify its own work** along the way?

Cherny calls verification "the single most important thing that people do not get right." A task with a verification loop will run; a task without one gets stuck. This is the mechanism behind [Long-Running Agents and Dynamic Workflows](../../agentic-coding/techniques/long-running-agents-and-dynamic-workflows.md) — the long horizon is downstream of good verification, not of clever prompting.

## The Anti-Pattern: Overengineering

- Engineers with years or decades of experience are the most prone to it — they try to over-specify and get the model to do the task exactly the way they would have.
- "That's just not the way the model works." Unlearning it is a journey.
- The right mental model is treating the model **like a coworker** — that's the level of intelligence it's at now.
- There is no "one weird trick." The approach is empirical: give it a hard task, give it verification tools, watch where it struggles, then fix that specific thing with better prompting, a skill, or an MCP for missing context.

Cherny's advice on where to learn this: "Don't listen to the LinkedIn influencers. Don't read Twitter."

## Core Insight

**The constraint on what AI products can do is rarely the model — it's the product.** At every generation there is a capability surplus sitting unused because no interface invites the model to express it, and often because the interface actively suppresses it.

This reframes product work as **subtraction plus elicitation**: remove the scaffolding you inherited from a weaker model, ask for something slightly beyond what you believe is possible, and give the model a way to check its own answer. The same subtractive discipline applied to prompts and tools is covered in [Ablation-Driven Harness Design](../../agentic-coding/techniques/ablation-driven-harness-design.md).

The corollary for founders: the next Claude Code is not gated on the next model. It's gated on someone noticing what the current one can already do.
