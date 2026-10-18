"""Acceptance tests for Journey 001. Run with unittest discovery."""
import unittest
from journey_001_representation import Framework, Item, Relation


class FrameworkTests(unittest.TestCase):
    def setUp(self):
        self.framework = Framework()
        self.framework.add_item(Item("a", "concept", "A"))
        self.framework.add_item(Item("b", "concept", "B"))

    def test_add_and_retrieve_item(self):
        self.assertEqual(self.framework.get_item("a").label, "A")

    def test_duplicate_item_id_is_rejected(self):
        with self.assertRaises(ValueError):
            self.framework.add_item(Item("a", "entity", "Another A"))

    def test_relation_requires_existing_endpoints_without_partial_write(self):
        with self.assertRaises(ValueError):
            self.framework.add_relation(Relation("a", "related_to", "missing"))
        self.assertEqual(self.framework.all_relations(), ())

    def test_relation_type_and_direction_are_preserved(self):
        self.framework.add_relation(Relation("a", "supports", "b"))
        self.assertEqual(self.framework.relations(source_id="a"),
                         [Relation("a", "supports", "b")])
        self.assertEqual(self.framework.relations(source_id="b"), [])

    def test_multiple_relation_types_between_same_items(self):
        self.framework.add_relation(Relation("a", "supports", "b"))
        self.framework.add_relation(Relation("a", "differs_from", "b"))
        self.assertEqual(len(self.framework.relations(source_id="a")), 2)

    def test_query_does_not_invent_relations(self):
        self.framework.add_relation(Relation("a", "supports", "b"))
        self.assertEqual(self.framework.relations(relation_type="causes"), [])

    def test_empty_required_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            Item("", "concept", "A")
        with self.assertRaises(ValueError):
            Relation("a", "", "b")


if __name__ == "__main__":
    unittest.main()
