from drawdown.generate.sequence import Sequence

class FixedSequence(Sequence):

    def __init__(self, value) -> None:
        self._value = value

    def next(self):
        return self._value