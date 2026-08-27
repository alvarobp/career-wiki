# Production Readiness Checklist

> A pre-ship gate, not a compliance ritual. If you can't check these boxes, you're not ready. If you check them without thinking, you've already failed.

Use this before every significant launch: new service, major feature, infra change, or anything that touches money, keys, or customer data.

---

## How to use this

Work through each section. For every `[ ]` you can't check: either fix it, or write down why it doesn't apply and get a second pair of eyes on that decision.

**Mandatory sections** (no exceptions): Observability, Alerting, Deployment & Rollback, Security.

**Conditional sections**: apply based on what your change touches.

---

## 1. Observability

You cannot operate what you cannot see. This section is mandatory.

**Signals are correctly typed**
- [ ] Duration + causality is in a **span**, not a log line with `duration_ms`
- [ ] Events with standalone meaning are **logs**, not attributes on a span
- [ ] Health-over-time questions are answered by **metrics**, not log queries

**Traces**
- [ ] Critical paths (payments, transfers, minting, auth) have 100% tail sampling — not probabilistic sampling
- [ ] Every log line on a critical path includes `trace.id`
- [ ] You are not reconstructing a trace out of logs with `requestId` + start/end messages — that's a trace in denial
- [ ] Span attributes follow OTel conventions for infra (`http.route`, `db.system`) and domain semantics for business (`payment.status`, `mint.result`)

**Logs**
- [ ] No private keys, seed phrases, auth tokens, or unmasked PII in any log line — ever
- [ ] Business events (payment completed, transfer failed, wallet created) are `INFO` logs treated as records of truth — never sampled, retained for years
- [ ] `ERROR` logs co-exist with an `ERROR` span — the failure is captured in both
- [ ] `WARN` means "recovered, but pay attention" — not "I wasn't sure if this was an error"
- [ ] `DEBUG` is off in production by default, opt-in per request or per service
- [ ] `TRACE` in production is a smell — you probably need spans

**Metrics**
- [ ] Metrics are built around your SLOs, not around what's easy to instrument
- [ ] You are tracking all four golden signals: Latency, Traffic, Errors, Saturation
- [ ] No `user.id`, `request.id`, or `order.id` in metric tags — cardinality explosion waiting to happen
- [ ] `tenant.id` is acceptable if bounded; `user.id` is almost never acceptable in metrics
- [ ] Every metric you expose has a clear action if it spikes or drops

---

## 2. Alerting

Alerts are a tax on human attention. Every alert you add is a withdrawal from your on-call team's trust account.

**Coverage**
- [ ] You have SLO-based alerts, not just static threshold alerts
- [ ] Fast burn (2h window, >14x burn rate) → pages immediately
- [ ] Slow burn (24h window, >3x burn rate) → creates a ticket, no page
- [ ] No alert fires on fewer than 5 minutes of sustained bad signal

**Quality**
- [ ] Every alert answers three questions without opening a dashboard: _what is broken_, _how bad_, _what to do first_
- [ ] Every alert has an owner team, severity, runbook link, and escalation path
- [ ] No alert dimensions include `user.id`, `request.id`, `trace.id`, or any high-cardinality field
- [ ] One service, one page — not one alert per pod, region, or replica

**Housekeeping**
- [ ] You have scheduled a post-launch alert review (within 30 days)
- [ ] If this is a new service: you have a plan for the first alert retro

---

## 3. Deployment & Rollback

Define your rollback rules before you deploy. Not during. Not after.

**Strategy**
- [ ] You have chosen a deployment strategy and can justify it:
  - Rolling update → default, fine for most services
  - Canary (5% → 25% → 100%) → when you can measure error rate + latency at each step
  - Blue/Green → only if stateless; never if rollback can cause data loss
- [ ] If canary: success and abort criteria are defined in numbers, not vibes

**Rollback rules (fill these in before you merge)**

| Threshold | Value |
|---|---|
| Max error rate before rollback | ___% |
| Max p99 latency before rollback | ___ms |
| Rollback time window | ___ hours |
| Auto-rollback enabled? | yes / no |

- [ ] The previous version can safely run against the new state (forward + backward compatible)
- [ ] You have confirmed: does this change touch the database?
  - If yes → Expand/Shadow/Reverse Shadow/Contract only. No shortcuts.
  - The Contract phase is where rollbacks die. Delay it.

**Feature flags**
- [ ] New behavior is behind a flag if rollback involves state
- [ ] Flag has a name prefix: `release_`, `exp_`, `ops_`, or `perm_`
- [ ] Flag has an owner, a creation date, and an expiration date (or cleanup ticket)
- [ ] Flag state is logged and has metrics per variant
- [ ] Flag is checked at a system boundary (controller/handler), not buried in business logic

**Before you hit merge**
- [ ] What state does this change touch?
- [ ] Can the previous version safely run against the new state?
- [ ] Is there a kill switch or degradation path?
- [ ] What metric decides rollback vs fix-forward?

---

## 4. Security

Non-negotiable. Especially in fintech/web3.

**Secrets & credentials**
- [ ] No secrets in source code, environment variable dumps, or log lines
- [ ] All credentials are short-lived or rotatable without a deploy
- [ ] Key material (private keys, seed phrases) never touches application logs or traces — at any level
- [ ] API keys for external providers have the minimum required permissions

**Access & IAM**
- [ ] Least privilege: this service/role has only the permissions it needs for this specific task
- [ ] Production access for engineers is time-bounded and purpose-bounded — no permanent wide-open access
- [ ] Any production mutation goes through a tool with dry-run, blast radius exposure, and audit trail
- [ ] No unfiltered access to PII/PHI — queries must filter or redact; access must be logged and justified

**Audit trail**
- [ ] Every production operation produces an audit record: who, when, what, why
- [ ] This is required for SOC 2 and PCI — not optional
- [ ] If you cannot answer "who did X on production last Tuesday", this box is unchecked

**Dependencies**
- [ ] Third-party dependencies scanned for known CVEs
- [ ] No direct dependency on a package with no maintained owner
- [ ] External service calls have timeouts and circuit breakers

---

## 5. Reliability & Failure Modes

**Graceful degradation**
- [ ] You know what happens when each of your dependencies is slow, unavailable, or returning errors
- [ ] Critical paths have circuit breakers or fallbacks — not just retries
- [ ] You have rate limiting on inbound traffic — not just on outbound calls

**Data & state**
- [ ] Idempotency is enforced on any operation that should not be applied twice (payments, transfers, mints)
- [ ] For fintech: financial reconciliation is automated or has a verified manual runbook
- [ ] For web3: you are not treating "transaction submitted" as "transaction succeeded" — chain confirmation is required
- [ ] Backups exist and have been tested with a restore in the last 90 days
- [ ] Data retention policy is defined and enforced (not just documented)

**Capacity**
- [ ] You have a rough estimate of peak load and your service's capacity against it
- [ ] Resource limits (CPU, memory) are set — unbounded containers are a time bomb
- [ ] You have tested behavior under load or have a plan to before GA

---

## 6. Incident Readiness

If you ship it, you support it. Before it goes live, the team needs to be able to respond.

**Runbooks**
- [ ] At least one runbook exists for the most likely failure mode
- [ ] Runbooks are in version control, close to the service, and linked from alert descriptions
- [ ] Every runbook has: goal, preconditions, exact steps, validation, rollback, escalation path
- [ ] A runbook without validation steps is a guess — don't ship a guess

**On-call readiness**
- [ ] On-call rotation is assigned and knows this service is live
- [ ] Escalation path is defined — not just "ping the team"
- [ ] For SEV-0/SEV-1 scenarios: IC and Ops Lead roles are pre-identified
- [ ] Fintech checklist items are documented (transfer pause, wallet isolation, circuit breaker locations)

**Postmortem hygiene**
- [ ] Previous incidents on similar systems have open action items tracked — review them before launch

---

## 7. Documentation

Operational docs exist to reduce time-to-action during incidents, not to satisfy audits. If it's not in Git, it doesn't exist.

- [ ] Service README exists and answers: what does this do, how do I run it, what does it own
- [ ] Architecture decision records exist for any non-obvious choices (infra, schema, external providers)
- [ ] Operational docs (runbooks, playbooks) are linked from the service README and from alert descriptions
- [ ] Every doc has an owner and a review cadence
- [ ] New docs written for this launch were reviewed by someone who will actually use them at 3am

---

## Final Gate

Before you ship, answer these four questions out loud:

1. **If this breaks at 2am on a Saturday, what does the on-call engineer do in the first 10 minutes?**
2. **If we need to roll back 4 hours after deploy, what exact steps do we follow, and what data might we lose?**
3. **If a customer's funds are affected, what is our detection time and our mitigation time?**
4. **If a regulator asks us what happened and why, can we reconstruct the full picture from our logs, traces, and audit trail?**

If you can answer all four confidently: ship it.

If you cannot: the system needs more work, not more courage.

---

*Owner: Infrastructure / SRE — Review cadence: Quarterly, or after any SEV-0/SEV-1 that reveals a gap.*

*See also: [Rollback Operations](Rollback-Operations.md) · [Deployment & Feature Flags](Deployment-and-Feature-Flags-rules.md) · [Observability](Observability.md) · [Alerting](Alerts-rules.md) · [Runtime Operations](RuntimeOperations.md) · [On-Call Checklist](Incidents/On-Call-Checklist.md)*
