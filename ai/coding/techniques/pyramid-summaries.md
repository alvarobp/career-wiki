# Pyramid Summaries

**Source:** [Software Factories — Techniques](https://factory.strongdm.ai/techniques) - StrongDM, February 2026

## Summary

Pyramid Summaries are reversible summarizations at multiple zoom levels. They compress context without losing the ability to expand back to full detail — providing agents with the right level of detail for each decision point.

## The Structure

A pyramid summary provides multiple layers of the same content:

- **Top level** — One-sentence essence (e.g., "Authentication service using OAuth2 with refresh tokens")
- **Middle levels** — Increasingly detailed summaries preserving key design decisions and interfaces
- **Base level** — Full source code or complete documentation

Agents navigate the pyramid based on what they need: scanning top-level summaries to find relevant areas, then drilling into detail only where needed.

## Why Reversibility Matters

Lossy summarization is dangerous for coding agents — critical details dropped from a summary can lead to subtle bugs or design violations. Pyramid summaries guarantee that any compressed representation can be expanded back to full detail, ensuring no information is permanently lost.

## Core Insight

Context windows are finite but codebases aren't. Pyramid summaries give agents a practical mechanism for managing large codebases: they can hold the shape of the whole system in context while drilling into detail where it matters. The key property is reversibility — compression without permanent information loss.
