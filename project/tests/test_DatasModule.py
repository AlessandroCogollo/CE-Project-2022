from unittest import TestCase
from project.utils import DatasModule as dm


class Test(TestCase):
    def test_get_datas(self):
        print(dm.DatasModule().hourly_producibility)
        self.fail()
