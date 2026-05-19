import unittest

from drawdown.strategy.ladder_strategy import LadderStrategy
from drawdown.source.state_pension import StatePension
from drawdown.generate.fixed_sequence import FixedSequence
from drawdown.source.money import Money

class LadderStrategyTest(unittest.TestCase):

    def test_excute(self)-> None:
        inflation = FixedSequence(value=0.02)
        currency = '£'
        year = 2028
        target = 40000
        state_pension_start = 2034

        strategy = LadderStrategy(
            target=Money(value=target, currency=currency),
            inflation=inflation,
            funds={},
            state_pension=StatePension(
                starting_year=state_pension_start,
                inflation=inflation,
                currency=currency
            )
        )

        amount = strategy.execute(year = year)

