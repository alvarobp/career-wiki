# Software Factory

**Source:** [Software Factories And The Agentic Moment](https://factory.strongdm.ai/) - Justin McCarthy (CTO, StrongDM), February 2026

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

## Related Concepts

- [Digital Twin Universe](../techniques/digital-twin-universe.md) — Behavioral clones of third-party services for validation
- [Gene Transfusion](../techniques/gene-transfusion.md) — Moving working patterns between codebases via exemplars
- [Shift Work](../techniques/shift-work.md) — Separating interactive from fully-specified work
- [Semport](../techniques/semport.md) — Semantically-aware automated code porting
- [Pyramid Summaries](../techniques/pyramid-summaries.md) — Reversible multi-level summarization
- [The Filesystem](../techniques/filesystem-as-agent-memory.md) — Files as agent memory substrate
- [Write-Only Code](../write-only-code.md) — The complementary idea that production code need not be read by humans
