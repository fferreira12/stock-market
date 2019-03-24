from abc import ABC, abstractmethod


class DataSource(ABC):
    """
    Designed to be the source of the data prices that the environment will use
    """

    def __init__(self, data):
        self._data = data

    @abstractmethod
    def next(self):
        raise NotImplementedError("method next not implemented")
