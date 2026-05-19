
class Money:
    """
        represents an amount of money
    """
    def __init__(self, value:int, currency:str):
        self._value = value
        self._currency = currency

    @property
    def total(self) -> int:
        return self._value

    @property
    def currency(self) -> str:
        return self._currency

    def equals(self, other:'Money') -> bool:

        return self._value == other.total and self._currency == other.currency

    def subtract(self, other:'Money') -> 'Money':

        if other.currency != self._currency:
            raise ValueError("Invalid currency")

        if other.total > self._value:
            new_amount = 0
        else:
            new_amount = self._value - other.total

        return Money(new_amount, self._currency)

    def add(self, other:'Money') -> 'Money':
        if other.currency != self._currency:
            raise ValueError("Invalid currency")

        return Money(self._value + other.total, self._currency)


    def multiply(self, value:float) -> int:
        """
            amount = 100_000_00
            value = 1.045
        """

        new_amount = int(round(self._value * value, 0))
        return Money(new_amount, self._currency)

    def __str__(self):
        #  return a string version
        return f"{self._currency}{self._value:,.2f}"
