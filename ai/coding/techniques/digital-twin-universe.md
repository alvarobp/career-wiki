# Digital Twin Universe (DTU)

**Source:** [Software Factories And The Agentic Moment](https://factory.strongdm.ai/) - Justin McCarthy (CTO, StrongDM), February 2026

## Summary

A Digital Twin Universe is a collection of behavioral clones of third-party services that replicate APIs, edge cases, and observable behaviors. Rather than mocking or stubbing external dependencies, DTUs faithfully reproduce the externally observable behavior of critical services, enabling validation at scale impossible against live systems.

## The Problem

Traditional testing against third-party services hits hard limits:

- **Rate limits** prevent high-volume validation
- **Abuse detection** blocks automated testing patterns
- **API costs** make exhaustive scenario coverage prohibitively expensive
- **Live services can't simulate failure modes** — you can't trigger arbitrary Okta outages or Slack edge cases on demand
- **Tests are too rigid** for LLM-based systems where behavior is probabilistic
- **Reward hacking** — agents can game narrow test suites, making validation unreliable

## The Approach

Clone the externally observable behaviors of critical third-party dependencies. StrongDM built DTUs for:

- Okta
- Jira
- Slack
- Google Docs
- Google Drive
- Google Sheets

These aren't simplified mocks — they're high-fidelity behavioral replicas that reproduce the actual APIs, edge cases, and observable behaviors of the real services.

## What DTUs Enable

- **Volume** — Validate at rates far exceeding production limits
- **Failure injection** — Test failure modes impossible against live services (outages, partial failures, race conditions)
- **Deterministic replay** — Replayable test conditions for debugging and regression
- **Cost elimination** — Thousands of scenarios per hour without API costs
- **Scenario holdout** — Scenarios stored outside the codebase (like ML holdout sets) prevent agents from gaming the validation

## The Economics Shift

Creating high-fidelity SaaS clones was always technically possible but never economically feasible before the agentic moment. The cost of building a behavioral clone of Okta or Jira would have been absurd as a manual engineering investment. With agents doing the implementation work, it becomes a practical infrastructure investment.

This exemplifies the factory principle of **deliberate naivete** — removing self-imposed constraints from the pre-agentic era.

## Core Insight

DTUs treat code validation like ML model validation: the system under test is opaque, and correctness is assessed purely through observable behavior against held-out scenarios. This reframing is essential when agents write the code — you can't rely on human code review, so you need validation infrastructure that's robust against both bugs and reward hacking.
