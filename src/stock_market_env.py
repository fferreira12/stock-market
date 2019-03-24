from gym.core import Env

from action import Action
from data_source import DataSource


class StockMarketEnv(Env):
    """
    The main class for the stock market environment.
    Should be compatible with the openAI Gym Env class.
    """

    def __init__(self, data_source, initial_cash: float = 1000):
        self._data_source: DataSource = data_source
        self._cash: float = initial_cash
        self._stock_amount: float = 0
        self._wealth = self._cash
        self._initial_wealth = self._wealth
        self._return = 0

    def step(self, action: Action, amount: float = 1.0):
        price = self._data_source.next()
        if action == Action.BUY and self.can_buy(amount, price):
            self._cash -= price * amount
            self._stock_amount += amount
        if action == Action.SELL and self.can_sell(amount):
            self._cash += price * amount
            self._stock_amount -= amount
        self._wealth = self._cash + price * self._stock_amount
        self._return = (self._wealth - self._initial_wealth) / self._initial_wealth
        return [self._cash, self._stock_amount, self._wealth, self._return]

    def reset(self):
        self._cash = self._initial_wealth
        self._stock_amount = 0
        self._wealth = self._cash
        self._return = 0

    def render(self, mode='human'):
        pass

    def close(self):
        pass

    def seed(self, seed=None):
        pass

    def can_buy(self, amount: float, unit_price: float):
        return self._cash >= amount * unit_price

    def can_sell(self, amount: float):
        return self._stock_amount > amount
