from drawdown.strategy.strategy import Strategy
from drawdown.simulate.target_income import TargetIncome
from drawdown.simulate.report_year import ReportYear
from drawdown.source.fund_source import FundSource
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
            strategy:Strategy,
            sources:dict[str, FundSource]
        ):
        self._year = year
        self._age = age
        self._period = period
        self._target = target
        self._strategy = strategy
        self._sources = sources

    def run(self) -> dict:
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
        result = {}
        for i in range(0, self._period):

            year = self._year + i
            age = self._age + i

            result[year] = self._run_year(
                year=year,
                age=age
            )
        return result

    def _run_year(self, year, age) -> ReportYear:

        report = ReportYear(year=year, age=age)

        for k, v in self._sources.items():
            report.set_funds(k, v)

        return report