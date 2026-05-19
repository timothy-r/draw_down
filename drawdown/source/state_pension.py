from drawdown.source.money import Money
from drawdown.generate.sequence import Sequence

class StatePension:

    def __init__(
        self,
        starting_year:int,
        inflation:Sequence,
        currency:str
    ):
        self._starting_year = starting_year
        self._inflation = inflation
        self._currency = currency

    def get(self, year:int) -> Money:
        return Money(value=0, currency=self._currency)