# Filesystem as Agent Memory

**Source:** [Software Factories — Techniques](https://factory.strongdm.ai/techniques) - StrongDM, February 2026

## Summary

Models can navigate repositories quickly and adjust their own context by reading and writing files. Directories, indexes, and on-disk state become a practical memory substrate for agents — more durable and inspectable than in-context memory alone.

## The Principle

Rather than trying to fit everything into the context window or relying on external memory databases, use the filesystem itself as the agent's memory and coordination layer. Files are:

- **Persistent** — survive across sessions and agent restarts
- **Inspectable** — humans can read and audit agent state
- **Navigable** — models are good at traversing directory structures
- **Writable** — agents can update their own context by creating and modifying files

## Applications

- **Indexes** — Agents maintain file indexes or summaries that help them navigate large codebases efficiently
- **State tracking** — Progress, decisions, and intermediate results stored as files
- **Coordination** — Multiple agents can read and write shared files for implicit coordination
- **Context management** — Agents compress and expand context by writing summaries and reading details on demand

## Core Insight

The filesystem is the most natural and practical memory substrate for coding agents. It's already the medium they work in — making it also the medium they think in aligns their capabilities with their environment.
