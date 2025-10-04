import abc

class Sequence(abc.ABC):
    """
        produces a variable value that fluctuates beween min & max
        and produces an average value over a specified period
    """

    @abc.abstractmethod
    def next(self) -> float:
        pass