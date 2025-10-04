import unittest
from drawdown.simulate.simulator import Simulator
from drawdown.simulate.target_income import TargetIncome
from drawdown.strategy.strategy import Strategy
from drawdown.simulate.report_year import ReportYear
from drawdown.source.investment_pot import InvestmentPot

class SimulatorTest(unittest.TestCase):

    def test_produces_reports(self) -> None:

        year = 2027
        age = 61
        period = 30
        target = TargetIncome(target=36000)
        strategy = Strategy()
        pension_value = 500000

        sources = {'pension':InvestmentPot(value=pension_value)}
        sim = Simulator(
            year=year,
            age=age,
            period=period,
            target=target,
            strategy=strategy,
            sources=sources
        )

        result = sim.run()

        self.assertEqual(period, len(result))
        for r in result.values():
            self.assertIsInstance(r, ReportYear)
