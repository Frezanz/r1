# Framework Filter: Truth, Time, Meaning, Value, and Mattering

**ID:** C-FILTER-001  
**Status:** Working design proposal; open to revision  
**Purpose:** A common record and decision procedure for adding, connecting, tagging, retrieving, and ordering items in r1.

## Core rule

Do not compress distinct questions into one rating.

- **Truth:** What is the claim's truth status, and on what grounds?
- **Time:** When does it apply, when was it observed, and when might it need review?
- **Meaning:** What does the item mean in its context?
- **Value:** What is good, useful, harmful, or desirable relative to an explicitly stated standard or goal?
- **Mattering:** What difference does the item make to a specified entity, process, question, or goal?
- **Evidence:** What supports or challenges it?
- **Confidence:** How strongly does the assessor currently endorse it, and why?
- **Relevance:** How directly does it bear on the current task?
- **Urgency:** How costly is delay, and how quickly might the item become stale?
- **Relations:** Which other items does it depend on, support, contradict, explain, or update?

These dimensions can interact, but none should be used as a hidden substitute for another. High value does not make a claim true; high confidence does not make it certain; recent information is not automatically more accurate; and low immediate relevance does not make an item false.

## Proposed item schema

An item may contain:

```text
Item {
  id
  raw_content
  content_type
  interpreted_meaning
  scope_and_conditions
  truth_status
  evidence_and_counterevidence
  assessment_method
  confidence_and_uncertainty
  provenance
  valid_time
  observation_time
  recorded_time
  revision_history
  dependencies_and_relations
  value_context
  mattering_context
  task_relevance
  urgency
  open_questions
}
```

This is a candidate schema, not a claim that every item needs every field. Fields can be unknown, conditional, disputed, or inapplicable. Preserve raw content so that later interpretations do not overwrite the original.

### Keep three time fields distinct

- **Valid time:** when the claim applies to the situation it describes.
- **Observation time:** when the relevant event or state was observed or measured.
- **Recorded time:** when the framework received or stored the information.

These can differ. For example, a report recorded today may describe yesterday's state. A later correction should append revision history rather than erase the earlier record.

## Initial truth-status vocabulary

Use explicit labels, with the scope and justification attached:

- **ASSERTED:** presented as a claim, but not yet adequately assessed.
- **SUPPORTED:** evidence or a valid derivation supports it under stated conditions; this is not a guarantee of truth.
- **CONTRADICTED:** relevant evidence or a derivation conflicts with it under comparable conditions.
- **CONDITIONAL:** its truth depends on explicitly stated conditions, definitions, scope, or time.
- **UNRESOLVED:** available information does not justify a stronger status.
- **RETRACTED / SUPERSEDED:** no longer endorsed in the current record; preserve why and when the status changed.

These labels describe the framework's assessment, not metaphysical degrees of truth. Multiple evidence sources may conflict, and one claim may need to be split into smaller claims before a status is defensible. Do not use UNKNOWN as a synonym for FALSE.

## Filter pipeline

1. **Capture:** preserve the original item and provenance.
2. **Type:** distinguish factual claims from definitions, questions, instructions, predictions, and value judgments.
3. **Interpret:** identify meaning, referents, assumptions, and scope.
4. **Temporalize:** record applicable interval and observation/recording times where known.
5. **Assess:** inspect evidence, derivation, source, counterevidence, and method limits.
6. **Status:** record supported, contradicted, conditional, unresolved, or another justified state.
7. **Connect:** create explicit dependencies, support links, conflicts, and causal claims only where warranted.
8. **Annotate:** record value, mattering, task relevance, urgency, and intended use separately.
9. **Act:** choose whether to retain, link, investigate, retrieve, prioritize, qualify, or retract the item for a stated purpose.
10. **Audit:** preserve the decision reason and revision trigger.

## Ordering rules

There is no universal order suitable for every task. The ordering procedure should declare its objective first.

- For a **fact-checking task**, prioritize unresolved or contradicted claims central to the question and inspect their evidence.
- For a **time-sensitive decision**, consider valid time, freshness, expected rate of change, and cost of delay.
- For a **formal derivation**, inspect dependencies and premises before conclusions.
- For a **learning task**, prioritize concepts that unlock dependent concepts, while keeping confidence and evidence visible.
- For a **risk-sensitive decision**, consider consequences of error and the asymmetry between false acceptance and false rejection.
- For a **knowledge archive**, preserve provenance and uncertainty rather than discarding items solely because their current truth status is unresolved.

Any numerical ranking must name the objective, inputs, units or scale, assumptions, and validation. A ranking score must not overwrite the item's separate dimensions.

## Questions that can change this design

- Is truth status best represented as categorical, multi-valued, probabilistic, or some combination?
- Can one item contain multiple claims with different truth statuses?
- What formal relationship connects valid time to truth conditions?
- How should conflicting perspectives be represented without treating all perspectives as equally accurate?
- When should new evidence update a claim, create a competing claim, or change only confidence?
- Can mattering be estimated without an explicit entity or goal relative to which it matters?
- Is value an intrinsic property, a relation to a goal/observer, or a family of different concepts?
- Which filtering operations are universal, and which are domain-specific?

## Design constraint

The filter is not the theory of truth. It is an inspectable mechanism for preserving the distinctions needed while the theory is researched. Its labels, schema, and ordering rules must remain revisable.
