# Semport

**Source:** [Software Factories — Techniques](https://factory.strongdm.ai/techniques) - StrongDM, February 2026

## Summary

Semport (semantic port) is a semantically-aware automated port of code between languages or frameworks. Unlike mechanical translation, semports preserve the intent and behavior of the original code while adapting to the idioms, patterns, and conventions of the target language or framework. Can be one-time or ongoing.

## One-Time vs Ongoing

- **One-time semport** — A migration from one language/framework to another (e.g., Python to Go, React class components to hooks). The source is abandoned after the port.
- **Ongoing semport** — Continuous synchronization where changes in the source are automatically ported to the target. Useful for maintaining implementations across multiple platforms.

## Why "Semport" and Not "Port"

Traditional ports are mechanical — they translate syntax. Semports are semantic — they translate intent. An agent performing a semport understands what the code does, not just how it's written, and produces idiomatic code in the target that preserves behavior.

## Core Insight

With agents, cross-language and cross-framework migration becomes a routine operation rather than a major project. This unlocks decisions that were previously impractical: choosing the best language for each context without worrying about porting cost.
