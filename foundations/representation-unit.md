# Candidate Primitive 001: Distinction Under a Criterion

**Status:** Working proposal; not a conclusion.

## 1. Why start here?

An intelligent system must discriminate between alternatives: two inputs, two states, two possible meanings, a prediction and an observation, or a relevant and irrelevant feature. This makes distinction a candidate starting point for representation.

However, "difference" alone is not enough. A system needs some way to determine *which* difference matters for a task. The same two things may be distinct under one criterion and equivalent under another.

## 2. Working definition

Let (X) be a set of candidate states or descriptions, and let (c) be a criterion. Define a binary distinction function:

[
D_c : X \times X \rightarrow \{0,1\}
]

where (D_c(x,y)=1) means that (x) and (y) count as distinct under criterion (c), and (D_c(x,y)=0) means that they count as equivalent under that criterion.

This is a minimal formal starting point, not a universal law. Depending on the task, the output may need to be graded, uncertain, multi-valued, or structured rather than binary.

If the criterion induces a well-behaved equivalence relation, it partitions (X) into equivalence classes. We must not assume every useful criterion has this property: context-sensitive or directional comparisons may violate symmetry or transitivity.

## 3. What this definition does—and does not—say

It does say:
- distinction is relative to a criterion;
- an encoded difference is not automatically meaningful for every task;
- representation depends partly on what the system is trying to preserve.

It does not say:
- distinctions are the ultimate constituents of reality;
- every entity can be reduced to a single binary difference;
- the criterion is known, objective, or correct;
- distinguishing inputs is sufficient for understanding, reasoning, or intelligence.

## 4. Candidate computational unit

For early experiments, represent a distinction record as:

[
d = (x, y, c, r, p)
]

where:
- (x,y): the alternatives being compared;
- (c): the criterion or context of comparison;
- (r): the result (for example, distinct, equivalent, or unknown);
- (p): provenance, such as an observation, supplied label, rule, or learned estimate.

This is a record schema, not a claim that five fields are irreducible. The record may later prove too verbose or insufficient.

A relation graph can then store distinctions and relations between represented items. Persistent "entities" could be tracked as clusters or patterns that remain identifiable across transformations, but that is a separate hypothesis requiring its own identity criteria.

## 5. Alternative starting points to compare

**A. Entity-first:** store objects/entities with properties and links.

**B. Distinction-first:** store criterion-dependent contrasts; infer or construct stable entities and relations from repeated patterns.

**C. State-transition-first:** store states and transitions; represent entities as trajectories through state space.

**D. Latent-vector-first:** learn dense representations from data and add explicit relations only when useful.

None is presumed superior. Option D is a serious baseline, not a straw man.

## 6. Failure modes to watch

- **Circularity:** defining a distinction using an entity while defining the entity using distinctions, without independent grounding.
- **Vagueness:** allowing the criterion to be changed after seeing the result.
- **Overgeneralization:** treating all forms of difference as the same operation.
- **Information loss:** compressing a rich continuous difference into a binary label.
- **Ungrounded symbols:** manipulating internal records without a reliable connection to observations, instructions, or outcomes.
- **Combinatorial explosion:** storing every possible pairwise distinction rather than selecting task-relevant ones.
- **False reduction:** assuming all cognition, physical reality, or semantics can be explained by this schema.

## 7. Open questions

1. Who or what supplies the criterion: designer, task, environment, learned model, or another process?
2. Can the system learn criteria and detect when a criterion is inappropriate?
3. What is the minimum information needed to preserve a distinction across time and context?
4. When should two records be merged as the same entity, and when should one entity be split?
5. How are uncertainty, missing information, contradiction, and changing evidence represented?
6. Does distinction-first encoding help with compositional generalization or knowledge revision enough to justify its overhead?

## 8. Provisional conclusion

A criterion-dependent distinction is a plausible *computational primitive to test*. It is not yet established as the most fundamental unit of intelligence or reality. The next step is to compare it with entity-first and latent-vector-first representations on a small, controlled task.
