import unittest
from drawdown.simulate.simulator import Simulator
from drawdown.simulate.target_income import TargetIncome
from drawdown.strategy.strategy import Strategy
from drawdown.simulate.report_year import ReportYear
from drawdown.source.investment_pot import InvestmentPot
from drawdown.source.money import Money
from drawdown.generate.fixed_sequence import FixedSequence

class SimulatorTest(unittest.TestCase):

    def test_produces_reports(self) -> None:

        year = 2028
        age = 62
        period = 30
        currency = '£'
        target = TargetIncome(target=36000)
        interest = FixedSequence(0.05)


        isa_value = Money(value=60000, currency=currency)

        pension_cash_fund_value = Money(value=90000, currency=currency)
        pension_managed_value = Money(value=140000, currency=currency)
        pension_consensus_value = Money(value=140000, currency=currency)
        pension_global_equity_value = Money(value=450000, currency=currency)

        sources = {

            'isa': InvestmentPot(
                    value=isa_value, name='cash_isa', type='', risk=0, interest_rate=interest
                    ),
            'pension_cash_fund': InvestmentPot(
                value=pension_cash_fund_value, name='pension_cash_fund', type='', risk=1, interest_rate=interest)

            }

        strategy = Strategy()


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
