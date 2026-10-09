# r1 — A Relational Framework for Reality and Intelligence

**Status:** Foundational research. All proposed primitives and architectures are provisional.

`r1` investigates whether a precise relational framework can become the basis of an intelligent system that is architecturally different from a conventional language model.

The ambition is not merely to describe reality with shared vocabulary. It is to discover representations and operations from which useful understanding, inference, learning, prediction, and action can be built.

## Research objective

Develop and test a computational framework in which language is an interface to structured representations of distinctions, entities, properties, relations, measurements, states, and change. The framework may use neural networks or language models where useful; replacing them is not a requirement. The goal is to test whether a different core representation and learning process produces measurable advantages.

## Non-negotiable research rules

1. Preserve the intent of the original ideas while making each claim precise.
2. Label statements as **founder hypothesis**, **working definition**, **established result**, **derivation**, **empirical result**, or **open question**.
3. Separate a mathematical primitive from a claim about what is fundamental in reality.
4. Define types, assumptions, operations, and validity conditions before relying on a formula.
5. Do not treat a shared word across domains as proof of a shared mechanism.
6. Seek counterexamples and compare against simpler explanations and existing methods.
7. Keep negative results. Revise or reject ideas when evidence requires it.
8. Measure computational claims against explicit baselines; conceptual elegance alone is not evidence of intelligence.

## Starting hypotheses

- **H1 — Relational measurement:** Measurement can be analysed in terms of relations, criteria, procedures, and results, but these parts may not collapse into one concept.
- **H2 — Conceptual structure:** Distinction, relation, state, change, perspective, and measurement may form a useful dependency structure.
- **H3 — Cross-domain structure:** Some formal patterns may transfer across domains while retaining domain-specific semantics.
- **H4 — Alternative intelligence architecture:** An explicit relational world model may improve some kinds of compositional reasoning, grounding, or knowledge revision compared with a language-model-only baseline.

These are hypotheses, not established findings.

## Research path

1. **Representation:** Identify the minimum information a computational unit must preserve.
2. **Structure:** Define entities, distinctions, properties, relations, and identity without circular definitions.
3. **Dynamics:** Represent state transitions, time, causes, and changes.
4. **Semantics:** Connect symbols and language to grounded or otherwise interpretable representations.
5. **Inference and learning:** Define how the system derives, updates, and tests beliefs.
6. **Evaluation:** Build small controlled experiments and compare against baselines.
7. **Scaling:** Only after small tests succeed, explore larger systems and multimodal data.

## Repository map

- [`foundations/`](foundations/README.md) — candidate primitives and dependencies
- [`concepts/`](concepts/README.md) — working definitions of key concepts
- [`architecture/`](architecture/README.md) — proposed computational design
- [`domains/`](domains/README.md) — cross-domain interpretations and limits
- [`method/`](method/research-protocol.md) — formalization and validation protocol
- [`research/open-questions.md`](research/open-questions.md) — unresolved questions and counterexamples
- [`experiments/`](experiments/001-representation-unit.md) — initial computational research plan
- [`CHANGELOG.md`](CHANGELOG.md) — major revisions

## First milestone

Investigate whether a **distinction under a criterion** can serve as a useful primitive for constructing representations, and whether entities can instead be treated as stable patterns of distinctions and relations. Compare this against starting with explicit entity/object records.

Do not assume either candidate is fundamental. The first goal is a precise, testable comparison—not a complete theory of reality.
