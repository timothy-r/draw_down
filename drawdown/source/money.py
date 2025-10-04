class Money:
    """
        represents an amount of money
    """
    def __init__(self, amount:int):
        self._amount = amount

    def total(self) -> int:
        return self._amount

    def multiply(self, value:float) -> int:
        """
            amount = 100_000_00
            value = 1.045
        """
        self._amount = int(round(self._amount*value,0))
        return self._amount
