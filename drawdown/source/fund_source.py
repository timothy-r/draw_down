import abc

class FundSource(abc.ABC):

    @abc.abstractmethod
    def total(self)-> float:
        pass

    @abc.abstractmethod
    def withdraw(self, amount:float) -> float:
        """
            returns the amount withdrawn
            may not be requested amount if funds are insuficient
        """
        pass

    @abc.abstractmethod
    def increase(self, percent:float) -> float:
        pass