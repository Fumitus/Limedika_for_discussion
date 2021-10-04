from Limedika_for_discussion.models.store import StoreModel
from Limedika_for_discussion.tests.unit.unit_base_test import UnitBaseTest


class StoreTest(UnitBaseTest):
    def test_create_store(self):
        store = StoreModel('test')

        self.assertEqual('test', store.name,
                         'Store name after creation does not equal constructor argument.')
