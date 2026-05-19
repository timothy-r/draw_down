from drawdown.strategy.strategy import Strategy
from drawdown.source.money import Money

class LadderStrategy(Strategy):
    """
        a simple implementation that withdraws from a cash fund
        and moves funds from higher risk to lower risk investments
        increases target income by inflation
    """

    def execute(self, year:int) -> Money:
        """
            try to withdraw target income into bank account using ladder strategy
            at the end increase target by current inflation
            return the drawdown amount
        """

        # state_pension = Money(value=0, currency='£')
        pension = self._state_pension.get(year=year)

        amount = self._draw_down(pension=pension)

        self._ensure_safety_net(pension=pension)
        self._balance_funds()
        self._increase_target()

        return amount

    def _draw_down(self, pension:Money) -> Money:
        """
            try to draw from cash funds, isas
            fall back to other funds
        """
        pass

    def _ensure_safety_net(self, pension:Money) -> bool:
        """
            try to ensure a safety net of twice target is in cash funds and / or ISAs
        """
        pass

    def _balance_funds(self) -> None:
        pass

    def _increase_target(self) -> None:
        pass
