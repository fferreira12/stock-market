from data_source import DataSource
from random import random


class RandomDataSource(DataSource):
    """
    Test class for generating random price values
    """

    def __init__(self, min, max, max_variation):
        super().__init__(None)
        self._min = min
        self._max = max
        self._max_variation = max_variation
        self._last = self._min + (self._max - self._min) * random()

    def next(self):
        self._last = self._last + random() * self._max_variation
        if self._last > self._max or self._last < self._min:
            self._max_variation = -self._max_variation
        if self._last > self._max:
            self._last = self._max
        if self._last < self._min:
            self._last = self._min
        return self._last
