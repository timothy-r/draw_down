from drawdown.source.fund_source import FundSource
from drawdown.source.money import Money
class InvestmentPot(FundSource):

    def __init__(self, value:Money) -> None:
        self._value = value

    def total(self) -> Money:
        return self._value

    def withdraw(self, amount:Money) -> Money:

        if amount > self._value:
            amount = self._value
            self._value = 0.0
        else:
            self._value -= amount

        return amount

    def increase(self, percent:float) -> float:
        self._value *= percent
        return self._value
