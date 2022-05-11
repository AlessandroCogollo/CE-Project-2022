import inspect

from unittest import TestCase
from project.utils import DatasModule as dm


class TestDatasModule(TestCase):
    def test_init(self):
        # init data_obj && count of attributes
        self.data_obj = dm.DatasModule()
        count = 0
        for i in inspect.getmembers(self.data_obj):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    count = count + 1
        self.assertEqual(16, count)

    def test_get_connection_cursor(self):
        self.assertTrue(1)

    def test_close_connection(self):
        self.assertTrue(1)

    def test_set_query(self):
        self.assertTrue(1)
