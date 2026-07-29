# Ablation-Driven Harness Design

**Source:** [Boris Cherny: Stop Hobbling Your AI](https://www.youtube.com/watch?v=qyPCVqFUyDo) - Y Combinator, 2026-07-27

## Summary

Boris Cherny, creator of Claude Code, describes how the Claude Code team rebuilds its harness with every model release: they delete the entire system prompt, bring it back line by line, and measure the impact of each line. They call this an **ablation** — an eval where you delete things to figure out their impact. With Opus 5 they deleted over 80% of the Claude Code system prompt, because most of it existed to correct behaviours that the new model simply gets right on its own.

The same advice applies to anyone building on models, not just harness authors: every six months, delete your CLAUDE.md, your skills, and your hooks, and see what the model does. Instructions written for a past model generation are dead weight the current model reads on every single turn. Evals last a bit longer than prompts, but they saturate too and eventually get thrown away.

## The Ablation Loop

The rebuild is a three-step cycle, done fresh for each model generation:

1. **Delete.** Strip the system prompt, tool prompts, CLAUDE.md, skills, hooks. Start from as close to nothing as the product allows.
2. **Use it.** Run the actual product against real work — your codebase, your customer agent flows. Don't guess which instructions the model needs; you won't predict it correctly.
3. **Add back only on repeated failure.** When you see the model stumble on the *same* thing repeatedly, that's when a line goes back in.

The bar for adding a line is deliberately high: **the model reads that instruction every single time you use it**, so it has to earn its place.

## Experimenting Yourself

- `claude --system-prompt <text>` lets you replace the system prompt entirely to experiment.
- `CLAUDE_CODE_SIMPLE=1` is an undocumented environment variable that strips all system prompts, **including the tool prompts**. The team uses it as their own ablation baseline.
- A finding from that ablation: **the model is slightly more intelligent without the prompts**. The prompts stay because they make the *product* behave the way a person using it would want — not because they make the model smarter.

## Why Prompts Don't Transfer Across Generations

- Every model is genuinely different — different behaviours, different personality.
- Prompt lines mostly encode corrections for a specific model's weak spots. Those weak spots move.
- The same churn applies to tools and harness code: the team unships tools regularly. Almost all of what remains in the Claude Code harness today is **safety, permissions, static analysis, and UI** — the behavioural scaffolding has been deleted.
- Contrast with traditional engineering: big up-front system design, large unit test suites, re-architectures measured in months or years. Models are more like **a living creature** — you get to know each generation and adjust the harness empirically.

## Evals Saturate Too

The instinct that "code and prompts churn but evals are permanent" is only half right:

- Evals **outlive the harness, but not by much** — maybe one to three model generations.
- Because the model is improving on an exponential, evals get **saturated** and then have to be thrown away and rebuilt.
- New evals come from the same empirical loop: use the product, watch where the model struggles, and build the eval set from those observations.

## Core Insight

Instructions are liabilities that accrue silently. Every line of CLAUDE.md, every skill, every hook was written to patch a model that no longer exists, and it costs context on every turn. The discipline is not writing better prompts — it's periodically deleting all of them and forcing each one to re-justify itself against the current model. Deleting is the measurement, which is why "be brave enough to press delete" is the actual skill; see [Product Overhang and Unhobbling](../../ai-engineering/principles/product-overhang-and-unhobbling.md) for why the leftover scaffolding actively suppresses capability, and [Long-Running Agents and Dynamic Workflows](./long-running-agents-and-dynamic-workflows.md) for what the unencumbered model turns out to be capable of.
