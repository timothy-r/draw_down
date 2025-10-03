class Variable:
    """
        produces a variable value that fluctuates beween min & max
        and produces an average value over a specified period
    """

    def __init__(self, average:float, min:float, max:float, period:int) -> None:

        self._average = average
        self._min = min
        self._max = max
        self._period = period

        # keep a record of generated values
        self._values = []

    def next(self) -> float:
        pass