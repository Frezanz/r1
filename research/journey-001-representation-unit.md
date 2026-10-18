# Journey 001 — Representation Unit

**Series:** r1 implementation journeys  
**Status:** First implementation experiment  
**Repository:** `Frezanz/r1`  
**Rule:** Add to the existing repository. Do not delete or overwrite previous work.

## Why this journey exists

We need to discover what the Framework must represent before adding reasoning, language understanding, memory, or learning. This journey implements the smallest testable candidate: identifiable items connected by explicitly typed relations.

This is an experiment, not a claim that a graph is intelligence or that relations explain all reality.

## Question

Can a minimal relational representation preserve distinctions and connections clearly enough to support later operations without silently inventing meaning?

## Scope

Implement only:
- an identifiable item with a declared kind and label;
- an explicitly typed relation between two existing items;
- a Framework that stores items and relations;
- validation against duplicate identifiers and relations to missing items;
- simple retrieval of relations;
- tests for the invariants above.

Do **not** implement natural-language interpretation, automatic inference, learned routing, emotions, concentration, self-modification, or a general-purpose formula engine in this journey.

## Initial representation contract

An item records:
- `id`: stable identifier within this Framework instance;
- `kind`: declared category, not a claim that the category is universal;
- `label`: human-readable description;
- `attributes`: optional explicit properties.

A relation records:
- `source_id`;
- `relation_type`;
- `target_id`;
- `attributes`: optional details about this particular relation.

The representation must not treat a relation as automatically true in the real world. It records what the system has been told or has explicitly constructed. Evidence and provenance are not yet fully modeled; that is a known limitation, not something to hide.

## Acceptance tests

1. Distinct items can be added and retrieved by identifier.
2. Duplicate item identifiers are rejected.
3. A relation can be added only when both endpoint items exist.
4. Relations retain their explicit type and direction.
5. Queries return matching relations without inventing new ones.
6. The same two items can have more than one relation type.
7. A failed operation must not leave a partially added relation behind.

## What this journey cannot prove

Passing these tests proves only that the data structure obeys its contract. It does not prove understanding, reasoning, generalization, or superiority to language models.

## What we learn next

After running the tests and examining awkward examples, decide whether the representation unit needs distinct structures for concepts, entities, states, measurements, events, evidence, uncertainty, or time. Add a distinction only when an example or operation requires it. These are candidates, not predetermined sublayers.

## Journey log

- **Start:** 2026-10-18
- **Starting point:** Existing r1 research and prototype history remain untouched.
- **First deliverable:** Minimal relational store with tests.
- **Exit condition:** Tests pass and limitations are documented before Journey 002 is named.
