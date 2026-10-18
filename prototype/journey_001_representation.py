"""Journey 001: a minimal, explicit relational representation.

This is a data-structure experiment, not an intelligence system.
It stores declared items and relations; it does not infer truth.
"""
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Item:
    id: str
    kind: str
    label: str
    attributes: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("Item id must not be empty")
        if not self.kind.strip():
            raise ValueError("Item kind must not be empty")
        if not self.label.strip():
            raise ValueError("Item label must not be empty")


@dataclass(frozen=True)
class Relation:
    source_id: str
    relation_type: str
    target_id: str
    attributes: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.source_id.strip() or not self.target_id.strip():
            raise ValueError("Relation endpoints must not be empty")
        if not self.relation_type.strip():
            raise ValueError("Relation type must not be empty")


class Framework:
    """Store explicit items and directed, typed relations."""

    def __init__(self) -> None:
        self._items: dict[str, Item] = {}
        self._relations: list[Relation] = []

    def add_item(self, item: Item) -> None:
        if item.id in self._items:
            raise ValueError(f"Duplicate item id: {item.id}")
        self._items[item.id] = item

    def get_item(self, item_id: str) -> Item:
        try:
            return self._items[item_id]
        except KeyError as exc:
            raise KeyError(f"Unknown item id: {item_id}") from exc

    def add_relation(self, relation: Relation) -> None:
        # Validate both endpoints before changing state: no partial writes.
        missing = [
            item_id for item_id in (relation.source_id, relation.target_id)
            if item_id not in self._items
        ]
        if missing:
            raise ValueError(f"Relation references unknown item(s): {missing}")
        self._relations.append(relation)

    def relations(
        self,
        *,
        source_id: str | None = None,
        relation_type: str | None = None,
        target_id: str | None = None,
    ) -> list[Relation]:
        """Return only stored relations matching the supplied filters."""
        return [
            relation for relation in self._relations
            if (source_id is None or relation.source_id == source_id)
            and (relation_type is None or relation.relation_type == relation_type)
            and (target_id is None or relation.target_id == target_id)
        ]

    def items(self) -> tuple[Item, ...]:
        return tuple(self._items.values())

    def all_relations(self) -> tuple[Relation, ...]:
        return tuple(self._relations)


if __name__ == "__main__":
    # These relations are explicitly entered, not inferred.
    framework = Framework()
    framework.add_item(Item("earth", "entity", "Earth"))
    framework.add_item(Item("sun", "entity", "Sun"))
    framework.add_relation(
        Relation("earth", "orbits", "sun", {"source": "example"})
    )
    for relation in framework.relations(source_id="earth"):
        print(f"{relation.source_id} --{relation.relation_type}--> {relation.target_id}")
