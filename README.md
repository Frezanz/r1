# r1 — A Relational Framework for Reality and Intelligence

**Status:** Foundational research. Definitions, primitives, and architectures remain provisional.

`r1` investigates how to build a formal framework for representing reality and developing intelligence independently of large language models. An LLM is not assumed to be the cognitive core, the source of meaning, or the authority that decides what is true. Neural networks, machine learning, and conventional computation are also not ruled in or out in advance; each must earn its place through argument and evidence.

The project aims to discover explicit representations and operations for understanding, inference, learning, revision, prediction, and action. It must not confuse a useful description of reality with a demonstrated mechanism of intelligence.

## First research target: truth

The first task is to investigate **what truth is and how truth can be assessed**. We must not assume that truth is identical to evidence, confidence, consistency, stability, usefulness, or consensus.

The investigation must distinguish at least:
- the truth of a proposition or claim;
- the evidence available for or against it;
- the system's current confidence and the reasons for that confidence;
- the conditions, scope, perspective, and time to which the claim applies;
- the practical value, meaning, and relevance of storing or using it.

These may be related, but they are not interchangeable. A true claim may be unverified; a well-supported claim may later be overturned; a stable claim may be false; and a useful claim is not thereby true.

See [the truth investigation](research/truth-first-investigation.md) and [the framework filter](concepts/framework-filter.md).

## The framework filter

Every candidate item entering the framework should be inspectable rather than accepted as an undifferentiated piece of information. The filter records, where applicable:

1. **Content and type:** What exactly is being added—observation, claim, definition, inference, hypothesis, question, or value judgment?
2. **Truth status:** What is asserted, supported, contradicted, conditional, or unresolved?
3. **Evidence and provenance:** What supports it, where did the information come from, and can the support be checked?
4. **Time:** When was it valid, observed, recorded, or revised? Is it time-sensitive or about change?
5. **Meaning and scope:** What does it mean, under which interpretation, assumptions, domain, and conditions?
6. **Value and mattering:** What difference would it make, to which goal or entity, and with what consequences?
7. **Relations and dependencies:** What does it depend on, contradict, support, explain, or change?
8. **Revision:** What observation or argument would require its status to change?

This is a **multi-dimensional record, not one universal truth score**. Truth assessment, uncertainty, value, urgency, and relevance must remain distinct until a justified rule connects them. Ordering should depend on the task and explicit priorities, not silently treat the most recent, useful, confident, or repeated item as the truest.

## Research discipline

1. Preserve the founder's intended meaning separately from later interpretations.
2. Mark each statement as a raw idea, working definition, hypothesis, formal result, empirical result, or open question.
3. Separate claims about reality from claims about formal systems and claims about computational performance.
4. State assumptions, scope, time conditions, and evaluation procedures.
5. Seek counterexamples and competing explanations; preserve negative results.
6. Do not treat shared vocabulary as proof of a shared mechanism.
7. Do not promote a hypothesis to an established result merely because it fits the framework.
8. Keep a traceable history of revisions and the reasons for them.

## Provisional research path

1. **Truth:** Investigate truth, truth conditions, and the limits of truth assessment.
2. **Assessment:** Define how evidence, uncertainty, contradiction, and revision are represented without confusing them with truth itself.
3. **Filtering:** Specify how truth status, time, meaning, value, mattering, and provenance govern storage, relations, retrieval, and ordering.
4. **Foundations:** Compare candidate primitives—including distinction, entity, relation, state, change, process, and measurement—without presuming one is ultimate.
5. **Dynamics and identity:** Investigate state, change, time, persistence, and spatiotemporal identity.
6. **Formalization:** Define types, operations, dependencies, and inference rules precisely.
7. **Experiments:** Test narrow claims with counterexamples and explicit baselines.
8. **Intelligence:** Only then assemble and evaluate mechanisms for learning, reasoning, prediction, decision, and action.

This order is a research strategy, not a claim that truth is ontologically prior to every other concept.

## Repository map

- [`concepts/`](concepts/README.md) — provisional concept specifications and framework-filter dimensions
- [`foundations/`](foundations/README.md) — candidate primitives and dependencies
- [`research/truth-first-investigation.md`](research/truth-first-investigation.md) — first investigation and its open questions
- [`research/open-questions.md`](research/open-questions.md) — unresolved research questions
- [`architecture/`](architecture/README.md) — candidate computational designs, not fixed assumptions
- [`domains/`](domains/README.md) — cross-domain interpretations and limits
- [`method/research-protocol.md`](method/research-protocol.md) — formalization and validation procedure
- [`experiments/`](experiments/001-representation-unit.md) — initial, limited representation experiment
- [`prototype/`](prototype/README.md) — a narrow executable probe, not the framework itself
- [`CHANGELOG.md`](CHANGELOG.md) — major changes and research decisions

## Current milestone

Produce a defensible account of **what we mean by truth, what can and cannot be measured about it, and how the framework should represent the difference**. Do not begin by assigning arbitrary numeric truth scores or treating any candidate primitive as settled.
