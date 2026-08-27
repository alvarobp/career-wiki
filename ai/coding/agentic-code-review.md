# Agentic Code Review

**Source:** [Agentic Code Review](https://addyosmani.com/blog/agentic-code-review) - Addy Osmani, 2026

## Summary

AI code generation has moved engineering's bottleneck from **writing** to **reviewing**. Agents emit code faster than humans can verify it, so verification — not generation — is now the leveraged skill. Osmani frames this as pro-AI realism rather than skepticism: the constraint isn't that agents write bad code, it's that understanding code never got cheaper while producing it did.

The data backs the squeeze. GitClear found 4x code output yielding only ~12% productivity gain, with the gap absorbed by review work. Faros AI reported churn up 861%, defect rates climbing from 9% to 54%, review duration up 441.5%, and zero-review merges up 31.3%. CodeRabbit measured 1.7x more issues in AI-written code than human-written code. The response isn't to slow generation down — it's to build a review system that scales with it.

## The Intent Gap

Agents reason through decisions and then **discard that reasoning**. The reviewer becomes the first human to see the code with no access to why it looks the way it does.

- Human-authored PRs carry implicit intent: the author can explain trade-offs, and the commit history encodes deliberation
- Agent-authored PRs arrive as finished artifacts with the deliberation deleted
- **Capturing agent decision logs** makes reconstructing intent cheaper — the reasoning is a reviewable artifact, not exhaust

## Restructuring Review

Osmani's recommendations reorganize review around risk and evidence rather than uniform per-diff scrutiny:

- **Tier review by risk, not by author** — a config change and a payments path deserve different gates regardless of who or what wrote them
- **Fast-fail expensive PRs** using predictive signals *before* they consume human review time
- **Require evidence up front** — an intent statement, test output, and proof of execution shipped with the PR, not requested in review comments
- **Keep PRs small** — instruct agents explicitly to produce reviewable diffs; agents will happily emit a 2,000-line change if unconstrained
- **Scrutinize test changes** — agents sometimes "fix" tests to match broken behavior rather than fixing the behavior
- **Hold CI gates strictly** — don't let agents weaken deterministic safeguards to make their own output pass
- **Humans own the merge** — AI review output is *data*; human judgment is *accountability*

## Human On the Loop, Not In It

The scaling move is **sampling and spot-checking** rather than reading every diff. Osmani uses Claude Code to triage his own incoming PRs, letting the model surface what deserves attention while he stays positioned above the loop rather than inside every iteration of it.

The limit is the fully closed loop:

- Model-reviews-model with no human anywhere is **"borrowed confidence"**
- Reviewer and author share **correlated blind spots** — the same training, the same failure modes, so the reviewer is structurally unable to catch what the author got wrong
- Agreement between two models is not independent verification; it's the same judgment twice

## Core Insight

**Writing got cheap; understanding stayed exactly as expensive.** Every productivity claim about agentic coding has to survive that asymmetry, and most don't — the throughput gain shows up as review debt somewhere downstream.

The durable advantage is a **trustworthy review system**, not maximum code output. That means: risk-tiered gates so scrutiny goes where it matters, evidence attached at PR time so intent doesn't have to be reconstructed, humans positioned *on* the loop to sample rather than *in* it to read everything, and a human at the merge because accountability can't be delegated to a model that shares its author's blind spots.
