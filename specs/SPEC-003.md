# SPEC-003

# Risk-Based Approval Engine

Version

0.1

---

## Purpose

Create a Risk-Based Approval Engine for KAVEEP-RO.

The engine must decide what level of approval is required before any repository action can be recommended or executed.

Evidence can support a decision.

Convergence can increase trust.

But convergence is not permission.

---

## Mission

Receive Proposal

↓

Classify Risk

↓

Check Evidence

↓

Check Policy

↓

Simulate Outcome

↓

Request Approval

↓

Allow Execution Only If Approved

---

## Core Rule

Evidence is not permission.

Convergence is not permission.

Confidence is not permission.

A repository action can only proceed when the required approval level is satisfied.

---

## Decision Layers

KAVEEP-RO must separate three layers:

### 1. Truth Layer

What does the evidence show?

This is handled by the Convergence Evidence Engine.

### 2. Risk Layer

How dangerous is the proposed action?

This is handled by the Risk-Based Approval Engine.

### 3. Permission Layer

Who or what is allowed to approve the action?

This must always respect human approval rules.

---

## Risk Categories

### Low Risk

Actions with minimal impact.

Examples:

- Fixing spelling
- Improving wording
- Adding comments
- Formatting documentation
- Creating non-destructive reports

Default approval requirement:

- May be recommended automatically
- Execution may still require repository policy approval

---

### Medium Risk

Actions that affect structure, behavior, or future maintenance.

Examples:

- Adding new SPEC files
- Updating README meaning
- Creating Issues
- Adding labels
- Modifying documentation structure
- Proposing dependency updates
- Refactoring non-critical code

Default approval requirement:

- Requires evidence review
- Requires clear recommendation
- Human approval recommended before execution

---

### High Risk

Actions that may affect repository behavior, safety, or continuity.

Examples:

- Changing safety rules
- Modifying approval logic
- Updating workflow files
- Changing CI behavior
- Creating release branches
- Changing architecture
- Modifying critical source code

Default approval requirement:

- Requires strong convergence
- Requires simulation report
- Requires explicit human approval before execution

---

### Critical Risk

Actions that may cause irreversible or destructive outcomes.

Examples:

- Deleting files
- Deleting branches
- Force pushing
- Merging pull requests
- Enabling auto-merge
- Changing repository permissions
- Removing approval gates
- Executing code with system access
- Publishing releases
- Overwriting important history

Default approval requirement:

- Requires critical convergence
- Requires safety review
- Requires explicit human approval
- Must never execute automatically

---

## Approval Levels

### Level A: Inform Only

KAVEEP-RO may report findings.

No repository change occurs.

### Level B: Recommend

KAVEEP-RO may recommend an action.

No repository change occurs.

### Level C: Prepare

KAVEEP-RO may prepare a draft plan, draft issue, or draft PR proposal.

Execution still requires approval.

### Level D: Execute With Approval

KAVEEP-RO may execute only after explicit human approval.

### Level E: Block

KAVEEP-RO must block the action and explain why.

---

## Approval Matrix

Low Risk

- Minimum convergence: Level 2
- Approval level: A, B, or C

Medium Risk

- Minimum convergence: Level 3
- Approval level: B or C
- Human approval recommended

High Risk

- Minimum convergence: Level 4
- Approval level: D
- Human approval required

Critical Risk

- Minimum convergence: Level 5
- Approval level: D or E
- Human approval required
- Automatic execution forbidden

---

## Human Approval Requirement

Human approval must be:

- Explicit
- Action-specific
- Recent
- Understandable
- Recorded when possible

Examples of valid approval:

- “Approve creating SPEC-004”
- “Yes, create this issue”
- “Merge PR #3”
- “Delete branch test-agent after review”

Examples of invalid approval:

- “Looks good”
- “Continue”
- “Do whatever”
- “Fix everything”
- “Make it work”
- Approval given for a different action

Ambiguous approval must be treated as no approval.

---

## Simulation Requirement

Before high-risk or critical-risk actions, KAVEEP-RO must produce a simulation report.

The simulation should include:

- Proposed action
- Files affected
- Repository areas affected
- Possible consequences
- Safety concerns
- Rollback difficulty
- Required approval level
- Recommended decision

Simulation does not grant permission.

---

## Block Conditions

KAVEEP-RO must block or escalate when:

- Evidence is missing
- Evidence conflicts are unresolved
- Risk is high or critical without approval
- Action violates repository Essence
- Action bypasses human approval
- Action rewrites history without reason
- Action attempts destructive behavior
- Action exceeds repository policy
- User intent is unclear for a destructive action

---

## Output

The engine should produce an Approval Report.

The report should include:

- Proposed action
- Risk category
- Required convergence level
- Current convergence level
- Approval level
- Human approval status
- Simulation required
- Block conditions
- Recommended next step

---

## Safety Rules

The Risk-Based Approval Engine must never:

- Treat confidence as permission
- Treat convergence as permission
- Treat silence as approval
- Treat vague approval as explicit approval
- Execute critical actions automatically
- Lower risk classification to make execution easier
- Ignore repository Essence
- Hide blocked actions

When uncertain, choose the safer path.

---

## Acceptance Criteria

SPEC-003 is accepted when KAVEEP-RO clearly defines how risk controls approval.

It must clearly explain:

- Decision layers
- Risk categories
- Approval levels
- Approval matrix
- Human approval requirement
- Simulation requirement
- Block conditions
- Approval report output
- Safety rules
