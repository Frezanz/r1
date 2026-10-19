# Journey 001 — Fundamental Characters: Purpose and Open Questions

**Status:** Purpose defined; implementation and experiments are in progress.

## Purpose

Fundamental Characters provide identifiable units from which the system can construct, tag, connect, and later interpret more complex structures.

The initial implementation uses Python's existing language environment as its working foundation. It should reuse Python's established character handling, tokenizer, parser, compiler, and runtime, while adding our own metadata and optional capabilities around them.

The aim is not merely to collect symbols. It is to make the units used by the environment discoverable and enrichable with structured information that can support later formulae, reasoning, context, and the Framework.

## Core distinctions

1. **Character identity:** the exact character or encoded sequence being processed.
2. **Token identity:** a unit recognized by Python's tokenizer, such as a name, number, operator, or delimiter.
3. **Syntax role:** how a token participates in a parsed Python structure.
4. **Metadata tags:** additional labels our system attaches to a character, token, or occurrence.
5. **Context and relationships:** information that helps determine what a token is doing in a particular expression or program.

These are related but not interchangeable. For example, `*` is a character; in `a * b`, Python recognizes it as a multiplication operator. Our metadata system may attach a role and relationships to that occurrence.

## Intended capabilities

- Register and identify Python-relevant characters and token forms.
- Automatically derive initial tags from Python's existing tokenizer and syntax structures.
- Keep original source unchanged and preserve Python's normal execution path.
- Store additional metadata separately so it can be queried or used when needed.
- Allow metadata to accumulate across different contexts without forcing one universal meaning onto a symbol.
- Preserve source positions and the context in which a tag was assigned.
- Provide a foundation for constructing formulae and connecting units through the Framework.
- Measure the added storage, processing time, and memory as the implementation develops.

## Design points to preserve

- Reuse Python's established capabilities instead of recreating equivalent machinery.
- A character's written identity is distinct from its contextual role.
- A tag records a classification or interpretation; it should retain enough context to explain why it was assigned.
- The same character may have different roles in different contexts.
- Keep added capabilities optional where practical.
- Preserve the original code and existing repository work.
- Record findings from implementation before adding new structures or sub-layers.

## Open questions to investigate

1. What exactly belongs in the initial registry: Unicode code points, Python token spellings, token types, or all of these as linked records?
2. Should metadata attach to a character identity, a token type, a specific occurrence in source code, or several of these?
3. Which tags can be assigned directly by Python's tools, and which require our own rules?
4. How should the system represent one visible symbol made from multiple Unicode code points?
5. How should a tag preserve the source location and context that justify it?
6. How should repeated occurrences share common metadata while keeping occurrence-specific information?
7. What is the smallest useful metadata format for later formula construction and Framework relations?
8. How will we verify that original source is unchanged and existing Python behavior is preserved?
9. What are the measured time, memory, and storage costs with tagging enabled and disabled?
10. Which new structures or sub-layers become necessary only after an experiment reveals a concrete need?

## First practical milestone

Given Python source code, the system should use Python's own tools to inspect it, generate an initial metadata record for recognized characters or tokens and their occurrences, and display the result without executing the inspected source.

A successful milestone should be runnable on the target Termux environment, covered by tests, and accompanied by a small example showing the source, the detected structure, the generated tags, and the measured resource use where practical.

## Findings log

Add dated observations here after running experiments. Separate observed behavior from hypotheses and unresolved questions. Do not mark an architectural claim as validated until an experiment supports it.
