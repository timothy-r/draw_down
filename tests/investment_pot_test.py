import unittest

from drawdown.source.investment_pot import InvestmentPot
from drawdown.source.money import Money
from drawdown.generate.fixed_sequence import FixedSequence
class InvestmentPotTest(unittest.TestCase):

    def test_withdraw_returns_deducted_value(self) -> None:

        name = 'pension'
        type = ''
        risk = 4

        amount = Money(value=500000, currency='£')

        interest = FixedSequence(0.05)

        pot = InvestmentPot(value=amount, name=name, risk=risk, type=type, interest_rate=interest)

        deduction = Money(value=30000, currency='£')

        result = pot.withdraw(amount=deduction)

        self.assertTrue(deduction.equals(result))

        total = pot.total()

        self.assertTrue(amount.subtract(deduction).equals(total))

    def test_cannot_withdraw_more_than_total(self) -> None:

        name = 'pension'
        type = ''
        risk = 4

        amount = Money(value=10000, currency='£')

        interest = FixedSequence(0.05)

        pot = InvestmentPot(value=amount, name=name, risk=risk, type=type, interest_rate=interest)


        deduction = Money(value=30000, currency='£')

        result = pot.withdraw(amount=deduction)

        self.assertTrue(amount.equals(result))

        total = pot.total()
        self.assertTrue(Money(value=0, currency='£').equals(total))

    def test_increase(self) -> None:

        name = 'pension'
        type = ''
        risk = 4

        amount = Money(value=10000, currency='£')
        interest = FixedSequence(0.05)

        pot = InvestmentPot(value=amount, name=name, risk=risk, type=type,interest_rate=interest)

        percent = 0.1
        result = pot.increase(percent=percent)

        self.assertEqual(result.total, amount.total * percent)

