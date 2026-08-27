# Shift Work

**Source:** [Software Factories — Techniques](https://factory.strongdm.ai/techniques) - StrongDM, February 2026

## Summary

Shift Work separates interactive work from fully specified work. When intent is complete — specs, tests, existing apps are all defined — an agent can run end-to-end without back-and-forth human interaction. The key insight is recognizing which work requires human dialogue and which can be delegated entirely.

## The Two Modes

- **Interactive work** — Exploration, clarification, design decisions, ambiguous requirements. Requires human-in-the-loop dialogue.
- **Fully specified work** — Implementation from complete specs, test writing from defined scenarios, migrations with clear targets. Can run non-interactively.

## The Practice

Invest human effort in making work fully specified (writing good seeds, defining scenarios, building validation harnesses), then hand off the specified work to run autonomously. This maximizes the leverage of human attention: humans do the thinking, agents do the building.

## Core Insight

The bottleneck isn't agent capability — it's specification completeness. The factory mindset shifts human effort from writing code to writing specifications clear enough that agents can execute without interaction.
