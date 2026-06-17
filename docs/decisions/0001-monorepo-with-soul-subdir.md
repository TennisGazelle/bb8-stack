# ADR 0001: Monorepo with temporary soul subdir

## Status

Accepted for scaffold.

## Context

The project is young and cross-layer refactors are expected. Splitting into many repositories now would add ceremony before the seams are proven.

The personality/constitution should eventually live in a separate Git repository/submodule so that changes are auditable and reviewed as a human-owned artifact.

## Decision

Use one monorepo for the stack. Keep `bb8-soul/` as a normal directory for now. Convert it to a Git submodule later.

## Consequences

- Easier early refactors.
- One PR can span agent, MCP, docs, sim, and ROS placeholders.
- Soul repo separation remains planned but does not block Milestone 0.
