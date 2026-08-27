# Harness Engineering

**Source:** [Context engineering with Dex Horthy](https://www.youtube.com/watch?v=Usufn8IQJgw) - The Pragmatic Engineer, 2026-07-15

**Companion piece:** [Token Harder vs Token Smarter](./token-harder-vs-token-smarter.md)

## Summary

**Harness engineering** is the layer above context engineering: if context engineering is about optimising the inputs to a single prompt, harness engineering is about **raising the floor so that every turn of the agent produces the best possible result**. Dex Horthy posted the term around October/November 2025; Viv (now at LangChain) had written about it independently a couple of weeks earlier.

The term immediately got blurry — some people took it to mean *building* a harness, others *building around* one. Martin Fowler's split resolves this cleanly, and it's the definition Dex endorses.

## Inner vs Outer Harness (Fowler's framing)

- **Inner harness** — the tool definitions and integration points that a coding agent itself exposes. What Claude Code, Codex, or Amp ship with: read file, write file, search, bash, etc.
- **Outer harness** — everything *you*, the human, build to customise that for your codebase, languages, and needs: slash commands, MCP servers, skills, how you organise the repo, the dev environment the agent runs in.

Cursor's background agents are a good example of the outer harness as product: they wrap the inner harness (the coding agent) with a sandbox, a browser, a video recorder, and orchestration.

> "Harness engineering just is like how do I raise the floor so that every single turn of this thing, the results are as good as possible."

## Why RL Coupling Made Claude Code Good

Dex's read on why Claude Code felt like a step change over earlier CLI coding agents:

- **The model and the harness were trained together.** Reinforcement learning with verifiable rewards (RLVR) tuned the model against the *specific* tool set in that harness.
- The model got very good at the harness's primitives — reading files, writing files, searching for files — because it solved thousands of problems through exactly those tools.
- That coupling, not raw intelligence, is what made it feel dramatically better than the CLI agents that preceded it.

The implication for outer-harness design: **your custom tools are not on equal footing with the built-in ones.** The model has been trained on the inner harness and merely instructed about yours.

## Maintainability: The Untrained Dimension

Models got very good along *one* axis. The axis they haven't improved on is the one that matters over months.

- Benchmarks are overwhelmingly SWE-bench-shaped: here's a commit in Django, here's an issue filed around that time, reproduce the human's fix. Verified by running unit tests.
- **The cost function of bad architecture can't be evaluated by running the unit tests.** It hits you three to six months later when nobody can change the software.
- Newer benchmarks help but aren't sufficient. Cognition's **frontier-code** adds two layers of model review — a judge checking functional equivalence to the golden patch, plus a code-quality judge — and **marathon** targets maintaining a codebase over time.
- Dex is sceptical of model-judged quality generally: ask a model if its own code is good and it says "yes, comprehensive, has unit tests." Ask it to review a coworker's PR and it finds problems. Sycophancy makes agentic code review a floor-raiser, not a guarantee.
- His proposed benchmark shape: **have the model build 20 features in a row, maintaining the codebase throughout, without knowing what's coming next** — like a real product team. Make it hard enough that frontier models fail by issue six or seven.

> "The labs are where the benchmarks are. If there is no benchmark that can convey to me *did this model write code that is going to make my codebase better or worse*, then that dimension doesn't improve."

## Core Insight

Harness engineering is leverage applied one level below the prompt: instead of writing a better instruction, you improve the environment so **every** instruction lands better. But the outer harness can only raise the floor — it can't supply a capability the model was never trained for. Since models were RL-trained to be excellent at *completing a change* and never trained to be good at *leaving a codebase maintainable*, no amount of harness engineering closes that gap. That's the structural argument for keeping humans at the design and program-structure checkpoints (see [Research, Plan, Implement (RPI)](./techniques/research-plan-implement.md)) rather than at the PR-review checkpoint alone.
