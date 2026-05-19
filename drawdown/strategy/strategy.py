import abc

from drawdown.source.money import Money
from drawdown.generate.sequence import Sequence
from drawdown.source.state_pension import StatePension
class Strategy(abc.ABC):
    """
        Strategy applies a specific strategy to solving the problem of how to obtain the target income

    """
    def __init__(
        self,
        target:Money,
        inflation:Sequence,
        funds:dict,
        state_pension:StatePension
    ):

        self._target = target
        self._inflation = inflation
        self._funds = funds
        self._state_pension = state_pension