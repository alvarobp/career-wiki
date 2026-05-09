# Gene Transfusion

**Source:** [Software Factories — Techniques](https://factory.strongdm.ai/techniques) - StrongDM, February 2026

## Summary

Gene Transfusion is the practice of moving working patterns between codebases by pointing agents at concrete exemplars. Rather than writing abstract specifications, you provide a reference implementation — a solution paired with a good example can be reproduced in new contexts.

## How It Works

Instead of describing what you want in prose, you show the agent a working implementation in another codebase (or another part of the same codebase) and ask it to reproduce the pattern in the target context. The agent extracts the underlying intent and adapts it to the new environment.

## Why It Works

- Concrete examples carry far more signal than abstract descriptions
- Working code encodes edge cases, error handling, and design decisions that specs often miss
- Agents excel at pattern recognition and adaptation across contexts
- Reduces specification effort — "do it like this" is often clearer than a detailed spec

## Core Insight

A solution paired with a good reference can be reproduced in new contexts. This is the software factory equivalent of transfer learning — existing working patterns are the most efficient seeds for new implementations.
