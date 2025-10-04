from drawdown.strategy.strategy import Strategy
from drawdown.simulate.target_income import TargetIncome
class Simulator:
    """
        executes a simulation using input parameters
        for a specified number of years
        producing a report of values per year
    """

    def __init__(self,
            year:int,
            age:int,
            period:int,
            target:TargetIncome,
            strategy:Strategy
        ):
        self._strategy = strategy

    def run(self):
        """
            run a simulation
            for each year generate a report row
        """
        # for each year
            # set up a record object
            # set initial values of sources - start of year
                # including state pension amount - using age
            # update target based on last period's returns
            # using a strategy calculate amounts to withdraw to achive target
            # withdraw from sources - start of year
            # update sources - end of year
            # record all values
