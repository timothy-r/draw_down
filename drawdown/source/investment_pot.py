from drawdown.source.fund_source import FundSource
from drawdown.source.money import Money
class InvestmentPot(FundSource):

    def __init__(
        self,
        value:Money,
        name:str,
        type:str,
        risk:int
    ) -> None:

        self._value = value
        self._name = name
        self._type = type
        self._risk = risk

    def total(self) -> Money:
        return self._value

    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> str:
        return self._type

    @property
    def risk(self) -> str:
        return self._risk

    def has_funds(self, amount:Money) -> bool:
        if amount.currency != self._value.currency:
            raise ValueError(f"Invalid currency. Pot currency = {self.value.currency}. Other currency - {amount.currency}")

        if amount.total<= self._value.total:
            return True
        else:
            return False

    def withdraw(self, amount:Money) -> Money:
        if amount.currency != self._value.currency:
            raise ValueError(f"Invalid currency. Pot currency = {self.value.currency}. Other currency - {amount.currency}")

        if amount.total > self._value.total:
            withdrawn = Money(value=self._value.total, currency=self._value.currency)

            self._value = Money(0, currency=self._value.currency)

        else:
            withdrawn = Money(value=amount.total, currency=self._value.currency)

            self._value = self._value.subtract(other=amount)

        return withdrawn

    def increase(self, percent:float) -> Money:
        self._value = self._value.multiply(value=percent)
        return self._value
