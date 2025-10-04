from drawdown.source.fund_source import FundSource

class PensionPot(FundSource):

    def __init__(self, value:float) -> None:
        self._value = value

    def total(self) -> float:
        return self._value

    def withdraw(self, amount) -> float:

        if amount > self._value:
            amount = self._value
            self._value = 0.0
        else:
            self._value -= amount

        return amount

    def increase(self, percent:float) -> float:
        self._value *= percent
        return self._value
