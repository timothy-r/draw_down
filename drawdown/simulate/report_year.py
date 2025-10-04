from drawdown.source.fund_source import FundSource

class ReportYear():
    """
        captures the data for a single year
    """
    def __init__(self, year:int, age:int) -> None:

        self._year = year
        self._age = age
        self._funds = {}

    def set_funds(self, name:str, source:FundSource) -> None:
        self._funds[name] = source.total()