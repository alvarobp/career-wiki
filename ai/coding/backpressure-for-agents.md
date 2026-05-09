# Don't Waste Your Backpressure

*Summary of principles from Moss's blog post*
https://banay.me/dont-waste-your-backpressure

## Overview

**Back pressure** refers to automated feedback mechanisms that help agents identify and correct mistakes independently. By maximizing back pressure in your workflows, you enable AI agents to self-correct through iteration, freeing engineers from manual review of every action.

## The Problem Without Back Pressure

When agents lack tools for self-correction, engineers become the bottleneck:
- Every agent action requires manual review
- Engineers spend their own cognitive resources providing corrections
- Complex work becomes unscalable
- The human becomes the feedback loop

## Creating Back Pressure

### Developer Tools Integration

Give agents access to execution environments that provide immediate feedback:
- **Bash commands** - Direct system interaction and error output
- **Build systems** - Compilation errors catch issues early
- **Test runners** - Automated validation of correctness
- **Linters and formatters** - Style and quality enforcement

### Type Systems

Expressive type systems provide structured feedback:
- Identify edge cases that might not be handled
- Prevent invalid states from occurring at compile time
- Serve as machine-checkable documentation
- Guide agents toward correct implementations

### Quality Error Messages

Languages that excel at clear compiler feedback:
- **Rust** - Detailed error explanations with suggestions
- **Elm** - Human-friendly error messages designed for learning
- **Python** - Clear stack traces and type error messages

Agents can learn from and act upon well-structured error output.

### Visual Feedback Tools

For UI work, connect agents to visual comparison tools:
- **Playwright** - Automated browser testing
- **Chrome DevTools** - Real-time rendering inspection
- MCP servers that bridge agents to visual feedback

Enable agents to compare expected versus actual rendering.

### Domain-Specific Validation

Specialized tools for correctness verification:
- **Proof assistants** (Lean) - Mathematical verification
- **Fuzzing** - For CUDA kernels and edge case discovery
- **Logic programming** - Constraint satisfaction verification
- **Property-based testing** - Automated invariant checking

## Core Insight

Design workflows where agents can loop independently through iterations until they achieve consistency. The goal is to maximize automated feedback so agents can:

1. Execute an action
2. Receive structured feedback
3. Analyze what went wrong
4. Attempt a correction
5. Repeat until success

This removes the engineer from the inner loop, allowing them to focus on higher-level guidance rather than manual error correction.

## Practical Application

When delegating to agents, ask:
- What feedback mechanisms exist for this task?
- How will the agent know if it made a mistake?
- Can the agent iterate independently, or will I need to intervene?
- What tools can I add to increase back pressure?

The more back pressure in your workflow, the more complex work you can safely delegate to agents.
