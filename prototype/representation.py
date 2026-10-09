"""Minimal prototype for criterion-dependent distinction records.

This module is a research probe, not an intelligence system. It tests one
small claim: the same pair of items can be equivalent under one criterion
and distinct under another, while missing evidence should remain unknown.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping


class DistinctionResult(str, Enum):
    DISTINCT = "distinct"
    EQUIVALENT = "equivalent"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class DistinctionRecord:
    left_id: str
    right_id: str
    criterion: str
    result: DistinctionResult
    evidence: str


def compare(
    left_id: str,
    right_id: str,
    criterion: str,
    left: Mapping[str, Any],
    right: Mapping[str, Any],
) -> DistinctionRecord:
    """Compare two item records under one named criterion.

    Missing attributes produce UNKNOWN. The function deliberately does not
    infer that missing values are equal, and it does not choose the criterion
    on behalf of the caller.
    """
    if criterion not in left or criterion not in right:
        return DistinctionRecord(
            left_id, right_id, criterion, DistinctionResult.UNKNOWN,
            f"Missing '{criterion}' value for at least one item.",
        )

    left_value = left[criterion]
    right_value = right[criterion]
    result = (
        DistinctionResult.EQUIVALENT
        if left_value == right_value
        else DistinctionResult.DISTINCT
    )
    return DistinctionRecord(
        left_id, right_id, criterion, result,
        f"{criterion}: {left_value!r} versus {right_value!r}",
    )
