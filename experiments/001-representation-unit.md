# Experiment 001 — What Should the System Represent First?

**Status:** Proposed. No results yet.

## Question

Does a distinction-first representation improve relational reasoning, transfer to new combinations, or revision after new evidence compared with an entity-first representation and a learned-vector baseline?

## Hypotheses

- **H1:** Distinction-first records may make criteria and comparison results explicit, improving tasks where the relevant criterion changes.
- **H2:** Explicit records may impose memory and runtime costs and may underperform dense learned representations on noisy or high-dimensional inputs.
- **H3:** Any advantage will depend on the task; no architecture should be declared generally superior from a single benchmark.

## Synthetic environment

Generate small worlds containing:
- entities with 2–5 discrete properties;
- binary and ternary relations;
- several criteria under which two entities may be equivalent or distinct;
- state changes across 3–6 time steps;
- incomplete observations and occasional contradictory reports.

Keep train and test combinations separate so the system cannot succeed by memorizing the exact combinations.

## Systems to compare

1. **Entity-first:** explicit entity/property/relation records.
2. **Distinction-first:** records of alternatives, criteria, results, and evidence; optional construction of entities from repeated patterns.
3. **Learned-vector baseline:** a compact neural representation trained on the same examples, with a fair inference interface.

Use comparable training data and report model size, memory, and inference cost. The baseline need not be an LLM for this first experiment.

## Tasks

- Determine whether two descriptions differ under a specified criterion.
- Answer questions requiring two or more relations.
- Generalize to unseen combinations of known properties and relations.
- Update a conclusion when new evidence contradicts an earlier observation.
- Report "unknown" when the evidence is insufficient, rather than guessing.

## Metrics

- accuracy by task;
- generalization accuracy on held-out combinations;
- revision accuracy after new evidence;
- calibration or uncertainty quality where measurable;
- memory footprint, latency, and number of stored records;
- error categories and examples.

## Controls

- Use identical train/test examples for all systems.
- Include trivial baselines and randomly shuffled controls.
- Prevent access to test labels during learning.
- Run multiple random seeds for learned systems.
- Publish task generator, seeds, configurations, and failures.
- Do not count hand-coded answers to the test cases as evidence for a general method.

## Decision rule

Adopt distinction-first as a useful component only if it produces a reproducible advantage on a clearly defined task or offers a justified trade-off. If it does not, revise the representation or reject the hypothesis. One synthetic benchmark cannot establish general intelligence or a universal theory.

## Next implementation step

Specify a tiny data schema and generate 100–1,000 synthetic examples. Before coding the full architecture, write down the exact question each task asks and the correct answer-generation rule.
