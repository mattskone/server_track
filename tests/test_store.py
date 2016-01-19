import unittest

import store


class StoreTest(unittest.TestCase):

    def setUp(self):
        store._store['foo'] = ['bar']
        store._store['baz'] = ['quux', 'norf']

    def test_get_item(self):
        self.assertEqual(store.get_item('baz'), ['quux', 'norf'])

    def test_add_item_new(self):
        store.add_item('spam', 'eggs')
        self.assertEqual(store._store['spam'], ['eggs'])

    def test_add_item_existing(self):
        store.add_item('foo', 'grault')
        self.assertEqual(store._store['foo'], ['bar', 'grault'])

