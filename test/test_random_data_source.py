import unittest

from random_data_source import RandomDataSource


class TestRandomDataSource(unittest.TestCase):

    def test_random_data_source_creation(self):
        rds = RandomDataSource(10, 20, 1)

    def test_random_data_source_limits(self):
        min = 10
        max = 20
        rds = RandomDataSource(min, max, 1)
        data = []
        for _ in range(0, 50):
            data.append(rds.next())
        all_higher_than_min = all(x >= min for x in data)
        all_lower_than_max = all(x <= max for x in data)

        self.assertTrue(all_higher_than_min)
        self.assertTrue(all_lower_than_max)
