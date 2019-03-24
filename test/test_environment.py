import random
import unittest

from action import Action
from random_data_source import RandomDataSource
from stock_market_env import StockMarketEnv

class TestRandomDataSource(unittest.TestCase):

    def test_environment_creation(self):
        rds = RandomDataSource(10, 20, 1)
        env = StockMarketEnv(rds, 1000)
        self.assertIsNotNone(env, "Environment should not be none")

    def test_environment_step(self):
        rds = RandomDataSource(10, 20, 1)
        env = StockMarketEnv(rds, 1000)
        last_result = None
        for x in range(50):
            action = random.choice(list(Action))
            last_result = env.step(action)
        self.assertIsNotNone(last_result)

    def test_reset(self):
        rds = RandomDataSource(10, 20, 1)
        env = StockMarketEnv(rds, 1000)
        last_result = None
        for x in range(50):
            action = random.choice(list(Action))
            last_result = env.step(action)
        self.assertIsNotNone(last_result)
        env.reset()
        self.assertTrue(env._cash == env._initial_wealth)
        self.assertTrue(env._stock_amount == 0)
        self.assertTrue(env._wealth == env._cash)
        self.assertTrue(env._return == 0)
