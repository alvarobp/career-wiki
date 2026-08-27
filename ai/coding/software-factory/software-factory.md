# Software Factory

**Sources:**
- [Software Factories And The Agentic Moment](https://factory.strongdm.ai/) - Justin McCarthy (CTO, StrongDM), February 2026
- [Loop Engineering](https://x.com/addyosmani/status/2064127981161959567) - Addy Osmani

- [Dex Horthy on context engineering, loops and software factories](https://www.youtube.com/watch?v=Usufn8IQJgw) - The Pragmatic Engineer Podcast

- [Own the Outer Loop](https://x.com/addyosmani/status/2074927530482835916) - Addy Osmani, July 2026

## Summary

A Software Factory is non-interactive development where specs + scenarios drive agents that write code, run harnesses, and converge without human review. The term describes a maturity level where software is "grown" rather than written — agents operate end-to-end from specification to validated artifact, with humans shaping intent rather than authoring code.

StrongDM's internal factory team (founded July 2025) observed that starting with Claude 3.5 Revision 2 (October 2024), long-horizon agentic coding workflows began to **compound correctness rather than error** — a phase transition from prior LLM behavior where errors of all varieties accumulated over time.

## The Kōan

Three forms of the same principle:

- **Mantra form:** "Why am I doing this?" (implied: the model should be doing this instead)
- **Rule form:** Code must not be written by humans. Code must not be reviewed by humans.
- **Practical form:** Spending $1,000 on tokens per human engineer today indicates room for improvement in factory maturity.

## The Principles: Seed → Validation → Feedback

Every software factory project follows this loop:

1. **Seed** — The initial specification. Can be a PRD, brief description, visual mockup, or existing codebase. The entry point for agent work.
2. **Validation Harness** — End-to-end validation mirroring the actual production environment, including customer interactions, system integrations, and economic factors.
3. **Feedback Loop** — Sample outputs are reintroduced as inputs, enabling self-correction. The cycle continues until holdout scenarios consistently pass.

**Tokens are the fuel.** Converting obstacles into model-understandable representations requires creative engineering. Input channels include: use traces, screen captures, conversation transcripts, incident replays, adversarial use, agentic simulation, just-in-time surveys, customer interviews, and price elasticity testing.

## Scenarios vs Tests

Traditional tests proved insufficient for factory-style development because:

- Tests stored in codebases can be lazily rewritten to match code
- Code can trivially pass narrowly written tests (e.g., `return true`)
- Tests are too rigid when building with LLMs and agent loops as design primitives
- Tests can be **reward hacked**, making validation vulnerable to model cheating

**Scenario:** An end-to-end user story, often stored outside the codebase (analogous to holdout sets in ML training). Intuitively understood and flexibly validated by LLMs. Coverage expands from basic tests through integration, regression, end-to-end, and behavioral tests.

**Satisfaction:** A probabilistic metric measuring what fraction of observed trajectories through all scenarios likely satisfy the user — replacing boolean test pass/fail with a gradient.

## Unconventional Economics

Creating high-fidelity SaaS clones, massive scenario suites, or other factory infrastructure was always technically possible but never economically feasible. Engineers historically self-censored such proposals.

The factory mindset requires **deliberate naivete**: removing habits, conventions, and constraints of "Software 1.0." What was unthinkable six months ago is now routine.

## The Dark Factory And What Broke

The endpoint of the factory is the **dark factory** — the term comes from manufacturing plants that are fully robotic and therefore need no lights, not even light switches. Raw materials in, cars out. Applied to software: no human reads any code. Review is replaced by agentic review, testing by agentic testing, and the whole system is treated as a black box where user complaints are the only signal that something is broken.

Dex Horthy's team at HumanLayer built exactly this in July 2025 and shut it down by November. The failure mode he reports: after three to six months of shipping with nobody reading the code, the codebase becomes easier to rewrite than to fix. The specific incident was a root cause that Opus 4.1 could not find no matter how sophisticated the prompting — a primary key routed through the system as the wrong type — and the team spent roughly three weeks re-onboarding into code they had stopped reading three months earlier.

His diagnosis is that the cost function of bad architecture is invisible to the training loop. Models improved dramatically on SWE-bench-shaped problems because harness and model were trained together, but bad program design does not fail a unit test — it hits three to six months later when the software has become hard to change. Agentic code review does not close the gap either: a model asked whether code is good tends toward sycophancy, and the model reading the code is the model that wrote it.

See [Token Harder vs Token Smarter](../token-harder-vs-token-smarter.md) for the framing of the dark factory as the maximum-utilization end of that axis, and the leverage-seeking alternative.

## Keeping The Lights On: The Human Verdict

Addy Osmani's *Own the Outer Loop* locates the same failure precisely: the factory with the lights off breaks at the checkpoint where a human would otherwise decide. His cut runs through the factory rather than around it. Inside the boundary, the agent inner loop investigates, implements, tests and reports — that is capability. What crosses the boundary is not code but **evidence**: the diff, the tests, the logs, the reasons. Outside, the engineer decides whether the work is worth doing, whether the evidence is sufficient, whether to ship, block or redirect — and then carries the consequence. That is agency.

Three terms carry the argument:

- **Quality** — the back pressure installed before the agents run: type checks, tests, hooks, sandbox limits, audit logs, monitors. The point is not to grant agents all the autonomy they could exercise, but only as much as the available back pressure can regulate.
- **Verdict** — the production decision at the boundary: ship, block, redirect, narrow, guardrail, or reject. The model may write the line; the verdict belongs to whoever owns the dependent system.
- **Answerability** — the guarantee that someone can explain what changed, why it was safe, and what happens if they are wrong. With hour-scale agentic runs, most decisions are never recorded as tokens, so reconstructing the chain after the fact is impossible; answerability has to be designed in rather than recovered.

The human is removed from the *inner* loop, not from the system. Osmani puts them in four loops instead: the **constraints loop** (what inputs, architectures, invariants), the **sampling loop** (how much output to review), the **audit loop** (what evidence to keep), and the **ownership loop** (which part of the production boundary is yours).

He reads the industry numbers as a gap rather than a plateau. Sonar's 2026 State of Code puts AI-generated or significantly AI-assisted code at 42% of commits, up from 6% in 2023; 96% of engineers say they do not fully trust AI code, but only 48% always verify it. GitLab's June 2026 accountability research finds 85% naming review and validation as the bottleneck and 92% reporting some governance problem, with governance usually applied after creation — after the risk has been accepted. Generation outran control.

Three hidden costs come with the leverage: **cognitive surrender** (Wharton, 1,372 people: when the AI was wrong, ~73% accepted it anyway and felt more confident), **cognitive debt** (Anthropic RCT, 52 engineers: 17 points lower comprehension, 50% vs 67%, when learning through AI-generated code), and the **orchestration tax** (spinning up parallel agents is cheap; the attention to steer, triage and verify them does not parallelize). These are the mechanism behind the dark factory's three-to-six-month failure: comprehension erodes silently while output does not.

His durability claim: speed and recall are already gone, verification is being automated, taste decays with each model release, but accountability does not decay at all. "The half-life of an edge is one release; the half-life of a signature is a career." Agents can choose, route, merge and escalate inside a policy — they cannot inherit the consequence.

## The Layer Above: Loop Engineering

Addy Osmani places [Loop Engineering](../loop-engineering.md) one floor above both the agent harness and the factory. The harness is the environment a single agent runs inside; the factory is the system that builds the software. A loop is that same system running on a timer, spawning its own helpers and feeding itself — an automation fires on a schedule, discovers work, hands it to sub-agents in isolated worktrees, and writes state back to disk so tomorrow's run resumes where today's stopped.

The framing matches the factory's own logic: you stop prompting the agent and instead design the system that prompts it. The memory lives outside the conversation (a markdown file, a board) because the model forgets between runs and the repo does not. Osmani is more cautious than the factory framing about what this removes — verification stays with the human, comprehension debt grows faster the smoother the loop runs, and two people building the same loop get opposite results depending on whether they use it to move faster on work they understand or to avoid understanding it.

## Related Concepts

- [Digital Twin Universe](../techniques/digital-twin-universe.md) — Behavioral clones of third-party services for validation
- [Gene Transfusion](../techniques/gene-transfusion.md) — Moving working patterns between codebases via exemplars
- [Shift Work](../techniques/shift-work.md) — Separating interactive from fully-specified work
- [Semport](../techniques/semport.md) — Semantically-aware automated code porting
- [Pyramid Summaries](../techniques/pyramid-summaries.md) — Reversible multi-level summarization
- [The Filesystem](../techniques/filesystem-as-agent-memory.md) — Files as agent memory substrate
- [Write-Only Code](../write-only-code.md) — The complementary idea that production code need not be read by humans
- [Loop Engineering](../loop-engineering.md) — The factory running on a timer, prompting itself

- [Token Harder vs Token Smarter](../token-harder-vs-token-smarter.md) — Maximising token throughput versus seeking leverage points