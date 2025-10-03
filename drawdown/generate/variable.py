import random
class Variable:
    """
        produces a variable value that fluctuates beween min & max
        and produces an average value over a specified period
    """

    def __init__(self, average:float, min:float, max:float, period:int) -> None:

        # assert that min < average < max

        self._average = average
        self._min = min
        self._max = max
        self._period = period

        # keep a record of generated values
        self._values = []
        diff = max - min
        step = diff / (period*2)
        self._population = []
        # weights prefer the central value
        # the middle value should be 0.5
        # calculate others spreading out lower & higher
        self._weights = []

        item = min

        for i in range(0, period*2):

            self._population.append(item)
            item = round(item+step,2)
            self._weights.append(1/(period*2))

        self._population.append(max)
        self._weights.append(1/(period*2))

        print(f"_population {self._population}")
        print(f"_weights {self._weights}")

    def next(self) -> float:
        return random.choices(
            population=self._population,
            weights=self._weights,
            k=1
        )[0]

        return random.uniform(self._min, self._max)