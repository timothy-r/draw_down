import abc

from drawdown.source.money import Money
class FundSource(abc.ABC):

    @abc.abstractmethod
    def total(self)-> Money:
        pass

    @abc.abstractmethod
    def withdraw(self, amount:Money) -> Money:
        """
            returns the amount withdrawn
            may not be requested amount if funds are insuficient
        """
        pass

    @abc.abstractmethod
    def increase(self, percent:float) -> Money:
        pass