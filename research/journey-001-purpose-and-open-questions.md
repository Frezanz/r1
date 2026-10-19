# Journey 001 — Fundamental Building Blocks: Purpose and Open Questions

**Status:** Core purpose refined; implementation and experiments remain in progress.
**Change note:** This document broadens the original character/token framing without deleting that work. Character and token handling remain one application of the layer.

## Purpose

Fundamental Building Blocks establish and expand the units, distinctions, properties, states, and configurations from which the system can represent, construct, inspect, and creatively explore things across domains—including constructions not explicitly predefined.

The purpose is not merely to collect symbols or identify characters. It is to provide a foundation for construction. Human-readable symbols, alphabets, numbers, and notation are ways to supply or express defined components, not the boundary of the layer.

The foundation should accommodate physical and chemical structures, mathematical and quantitative objects, symbols and encodings, patterns, abstract concepts, and imaginary or hypothetical constructions. It should also permit new primitives or representational distinctions to be proposed when existing ones cannot adequately express a demonstrated need.

## Core distinctions

1. **Unit identity:** what distinct unit or primitive is being represented.
2. **Properties and states:** characteristics of a unit or its current condition.
3. **Relations:** connections or interactions between represented items.
4. **Configuration:** an arrangement of units and relations into a larger construction.
5. **Representation/encoding:** a symbol, string, diagram, or data structure used to express a construction.
6. **Context and constraints:** assumptions and rules that affect interpretation, compatibility, or validity.
7. **Provenance/status:** whether a construction is observed, sourced, inferred, hypothesized, invented, or unverified.

These are related but not interchangeable. For example, a chemical formula written as text is an encoding; a molecular structure includes atoms and bonds and may require geometry and constraints beyond that string.

## Candidate scope

- Physical structures and systems.
- Chemical elements, bonds, compounds, and reactions.
- Mathematical objects, quantities, dimensions, variables, and operations.
- Symbols, characters, numbers, notation, signals, and encodings.
- Patterns, sequences, symmetry, and configurations.
- Abstract entities, distinctions, properties, and concepts.
- Imaginary entities, hypothetical scenarios, and fictional rule systems.
- Relations, processes, and transformations when required to define a construction.

These are candidate domains, not separate required sub-layers. Their categories may overlap.

## Intended capabilities

- Represent identifiable units and distinguish identity from properties.
- Combine units into structured configurations.
- Represent a construction independently of any single human-readable encoding where practical.
- Preserve constraints relevant to a domain or explicitly declared fictional system.
- Propose new primitives when a concrete construction cannot be adequately represented with existing ones.
- Make constructions available to Formulae, Reasoning Formulae, Context, and the shared Framework.
- Preserve provenance and distinguish generated candidates from validated knowledge.
- Retain the existing Python character/token work as a practical human-readable and machine-readable application, preserving source and metadata separately.
- Measure representational coverage, validity, novelty, resource cost, and failure modes.

## Design points to preserve

- Do not equate symbols with the things they represent.
- Do not assume all domains share one universal primitive vocabulary before testing.
- Do not confuse a possible fictional construction with physical possibility or real-world truth.
- Do not treat a generated candidate as validated knowledge.
- Keep domain constraints and evidence explicit.
- Add sub-layers only when an observed need or experiment justifies them.
- Preserve previous repository work and distinguish observations from hypotheses.

## Relationship to the wider architecture

- **Formulae** organize and operate on available building blocks.
- **Reasoning Formulae** derive, compare, test, and revise candidate constructions.
- **Context** specifies applicable assumptions, constraints, interpretations, and state.
- **Framework** provides shared relational structure; it is not another sequential stage.
- **Output** renders constructions in human-readable or machine-usable forms.

These boundaries remain provisional until concrete examples and experiments test them.

## Open questions

1. What is the minimal set of distinctions needed to represent units, properties, relations, configurations, and encodings?
2. How should a primitive be defined relative to a representational system?
3. When should the system propose a new primitive rather than compose existing ones?
4. How can identity persist across different encodings or representations?
5. How should domain-specific constraints be expressed without hard-coding every possible domain?
6. How should physical validity, mathematical validity, fictional consistency, and speculation be distinguished?
7. What evidence is required before a generated construction can be treated as reliable?
8. Which responsibilities belong in this layer versus Formulae, Reasoning Formulae, Context, or Framework?
9. What experiments would demonstrate novel construction rather than mere retrieval or recombination?
10. How should coverage, novelty, validity, resource cost, and failure modes be measured?

## First practical milestone

Compare four contrasting constructions: a symbolic expression, a chemical structure, a mathematical object, and an imaginary entity. For each, record units, properties, relations/configuration, constraints, provenance/status, and a human-readable rendering. Identify shared representation needs and genuine domain differences before adding new sub-layers.

## Findings log

Record dated observations from experiments. Separate observed behavior from hypotheses and unresolved questions. Do not mark a capability as validated until an experiment supports it.
