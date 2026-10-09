# Research and formalization protocol

## Goal

Develop a framework whose definitions, inference rules, and models are explicit enough to evaluate coherence, consistency, explanatory usefulness, and (where applicable) completeness.

## Workflow for every concept

1. **Capture intent.** Preserve the founder's wording and intended meaning separately from later interpretations.
2. **Disambiguate.** List meanings and domains; identify ambiguity rather than silently choosing one.
3. **Review prior work.** Identify established mathematical or scientific definitions and relevant sources.
4. **Define the type.** Specify whether the concept is an entity, property, relation, function, process, proposition, measurement procedure, or model.
5. **Formalize.** Propose definitions, signatures, axioms, mappings, or equations.
6. **Check dependencies.** Find hidden assumptions, circular definitions, and undefined terms.
7. **Derive consequences.** State what follows from the formalization and its premises.
8. **Test examples and counterexamples.** Include edge cases and competing interpretations.
9. **Map domains.** Explain where a formal structure transfers and where it does not.
10. **Revise and version.** Record why a definition changed and which earlier claims it affects.

## Status labels

- `RAW IDEA`
- `WORKING DEFINITION`
- `FORMALIZED`
- `TESTED IN DOMAIN`
- `SUPPORTED`
- `CONTRADICTED`
- `DEPRECATED`

These labels describe research status, not certainty independent of context.

## Formal quality criteria

- **Well-defined:** symbols and terms have explicit meanings.
- **Coherent:** concepts fit together without unexplained semantic shifts.
- **Consistent:** no contradiction is derivable under the stated axioms and inference rules, subject to the chosen logic.
- **Complete:** only meaningful relative to a specified language and consequence relation; the project must state what completeness means before claiming it.
- **Explanatory:** the framework clarifies cases rather than merely renaming them.
- **Discriminating:** it distinguishes cases that should differ.
- **Testable where empirical:** it yields observations or outcomes that could count against it.
- **Traceable:** sources, assumptions, derivations, and revisions can be audited.

## Versioning discipline

Use Git history for changes. Preserve prior formulations when a substantive change alters meaning. Mark uncertain claims as uncertain. Never upgrade a hypothesis to an established result solely because it fits the framework.