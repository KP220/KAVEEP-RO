# SPEC-008

# Orchestration & Decision Pipeline Engine

Version

0.1

---

## Purpose

Create an Orchestration & Decision Pipeline Engine for KAVEEP-RO.

The engine coordinates all KAVEEP-RO analysis engines into a clear decision pipeline.

It must decide which engines are needed, in what order they should run, how their reports are combined, and when a decision must be escalated.

The Orchestration Engine coordinates decisions.

It does not approve decisions by itself.

It does not execute actions by itself.

---

## Mission

Receive Task

↓

Classify Task Type

↓

Select Required Engines

↓

Run Analysis Pipeline

↓

Collect Reports

↓

Detect Conflicts

↓

Build Decision Package

↓

Escalate to Approval Engine

↓

Return Final Recommendation

---

## Core Rule

The Orchestration Engine is a coordinator.

It is not an approver.

It is not an executor.

It must never turn analysis into permission.

---

## Engine Boundaries

The Orchestration Engine must respect engine ownership.

### Repository Identity Engine

Owns repository identity definition.

### Convergence Evidence Engine

Owns evidence collection, classification, independence, and convergence level.

### Specification Compliance Engine

Owns compliance against approved SPECs.

### Continuity Guardian Engine

Owns continuity and identity drift assessment.

### Risk-Based Approval Engine

Owns risk classification, approval level, and block conditions.

### Swarm Consensus Engine

Owns independent multi-agent reasoning and consensus formation.

### Pull Request Intelligence Engine

Owns pull request analysis and PR-specific recommendation packaging.

The Orchestration Engine must not duplicate these responsibilities.

---

## Task Types

The engine must support different task types.

### 1. Repository Review

Used when reviewing the overall state of a repository.

Pipeline:

Repository Identity Engine

↓

Convergence Evidence Engine

↓

Specification Compliance Engine

↓

Continuity Guardian Engine

↓

Risk-Based Approval Engine

---

### 2. Pull Request Review

Used when reviewing a pull request.

Pipeline:

Pull Request Intelligence Engine

↓

Convergence Evidence Engine

↓

Specification Compliance Engine

↓

Continuity Guardian Engine

↓

Risk-Based Approval Engine

↓

Swarm Consensus Engine if risk is high or critical

---

### 3. Issue Creation

Used when deciding whether to create or recommend a GitHub Issue.

Pipeline:

Convergence Evidence Engine

↓

Risk-Based Approval Engine

↓

Orchestration Decision Package

---

### 4. Release Decision

Used when deciding whether a repository is ready for release.

Pipeline:

Specification Compliance Engine

↓

Convergence Evidence Engine

↓

Continuity Guardian Engine

↓

Risk-Based Approval Engine

↓

Swarm Consensus Engine

---

### 5. Governance Review

Used when identity, safety, approval, or continuity becomes uncertain.

Pipeline:

Repository Identity Engine

↓

Convergence Evidence Engine

↓

Specification Compliance Engine

↓

Continuity Guardian Engine

↓

Risk-Based Approval Engine

↓

Swarm Consensus Engine

---

## Pipeline Rules

The engine must follow these rules:

- Identity must be checked before continuity.
- Evidence must be collected before convergence is claimed.
- Compliance must use evidence, not assumptions.
- Risk classification must happen before approval.
- Swarm review is required for high-risk and critical-risk decisions.
- Human approval is required before execution.
- Missing evidence must stop automatic recommendation.
- Critical conflicts must block the decision package.

---

## Decision Package

The engine should produce a Decision Package.

The package should include:

- Task type
- Input summary
- Engines used
- Reports collected
- Conflicts found
- Missing evidence
- Compliance state
- Continuity state
- Risk classification
- Consensus level if applicable
- Approval requirement
- Block conditions
- Final recommendation

---

## Conflict Handling

The engine must detect cross-engine conflicts.

Examples:

- Evidence Engine reports weak convergence, but PR Engine recommends approval.
- Compliance Engine reports non-compliance, but Risk Engine classifies low risk.
- Continuity Guardian reports identity drift, but PR Engine says ready.
- Swarm Consensus contains safety objection, but approval package ignores it.

Conflicts must be included in the Decision Package.

Unresolved conflicts must block or escalate the decision.

---

## Escalation Rules

The engine must escalate when:

- Evidence is insufficient
- Engine reports conflict
- Risk is high or critical
- Continuity is diverging or broken
- Compliance is non-compliant or unknown
- Swarm reports minority safety concern
- Human approval is missing
- User intent is unclear for risky action

Escalation may include:

- Request more evidence
- Request human review
- Request governance review
- Block action
- Create follow-up issue
- Recommend audit

---

## Output States

### Inform

The system reports findings only.

### Recommend

The system recommends a next action.

### Prepare

The system prepares a draft action package.

### Await Approval

The system requires explicit human approval.

### Block

The system blocks the action.

### Unknown

The system cannot determine enough to recommend action.

---

## Safety Rules

The Orchestration Engine must never:

- Approve actions
- Execute actions
- Hide conflicts
- Ignore missing evidence
- Skip required engines
- Skip approval requirements
- Treat recommendation as permission
- Let one engine override another silently
- Allow critical actions without explicit human approval

When systems disagree, report the disagreement.

When evidence is missing, report uncertainty.

When risk is high, escalate.

---

## Acceptance Criteria

SPEC-008 is accepted when KAVEEP-RO clearly defines how all analysis engines are coordinated into decision pipelines.

It must clearly explain:

- Engine boundaries
- Task types
- Pipeline rules
- Decision Package
- Conflict handling
- Escalation rules
- Output states
- Safety rules
