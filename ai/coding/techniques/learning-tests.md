# Learning Tests

**Sources:**
- [AI That Works](https://podcasters.spotify.com/pod/show/ai-that-works) podcast
- Michael Feathers, *Working Effectively with Legacy Code*

## Summary

Learning Tests are small tests written against external systems to discover how they actually behave — not how you think they behave. Some are throwaway (quick explorations you delete once you've learned what you need), others are worth keeping as living documentation of how external dependencies work.

## When to Use

- Black-box APIs, SDKs, or CLIs where you can't read the source
- External dependencies with incomplete, outdated, or misleading documentation
- Any system where the cost of a wrong assumption is high (complex integrations, third-party services, unfamiliar frameworks)

## Practical Examples

- Test how an SDK handles session continuation — does resuming a session reuse or generate a new ID?
- Test how a crypto library behaves when HMAC input lengths don't match
- Test how an LLM API preserves or removes thinking tokens across conversation turns
- Test how a CLI tool behaves with edge-case inputs that aren't covered in docs
- Add these as test cases in your existing test suite — leverage the runner, assertions, and setup/teardown you already have

## Throwaway vs. Persistent

Not all learning tests have the same lifecycle:

- **Throwaway** — Quick explorations to answer a specific question. Write them, run them, learn from them, delete them. Good for one-off investigations or early research before you know what matters.
- **Persistent** — For dependencies you use heavily or that have subtle behavior, keep the learning tests in your test suite as executable documentation. They document your **contract with external systems you don't control**. Don't run them in every CI build — run them on demand when you suspect a contract has changed (e.g., upgrading a dependency, debugging an integration, or a new SDK version drops). Grow them incrementally: every time an external contract breaks you, add another learning test. These tests also serve as **reference material** — both humans and coding agents can read them to understand how to correctly use a library before writing application code.

The decision is simple: if you'll reference this behavior again, keep it. If it was a one-time question, toss it. You don't need to cover every library — focus on dependencies that like to change APIs or that behave as black boxes (CLIs, APIs with undocumented edge cases, probabilistic systems like LLM APIs).

## Application to Agentic Coding

Have agents write and run learning tests during research, before implementation begins. This shifts discovery of wrong assumptions from implementation (expensive rework) to research (cheap experiments). Especially valuable because agents operate from training data that may be stale — a learning test grounds them in the system's current reality.

Agents can also **generate** persistent learning tests. If you already have a few learning tests as examples, prompt an agent: "read the docs and the existing learning tests, then create a learning test that demonstrates how to use [new API] and documents its behavior." The agent reads existing tests for style and scope, reads the docs, and produces a new test — fast bootstrapping of your contract documentation.
