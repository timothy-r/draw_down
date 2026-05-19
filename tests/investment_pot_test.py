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

    def test_transfer(self) -> None:

        name = 'pension'
        type = ''
        risk = 4

        pot_a_amount = Money(value=500000, currency='£')
        interest = FixedSequence(0.1)

        pot_a = InvestmentPot(value=pot_a_amount, name=name, risk=risk, type=type,interest_rate=interest)

        name = 'pension'
        type = ''
        risk = 1

        pot_b_amount = Money(value=100000, currency='£')
        interest = FixedSequence(0.03)

        pot_b = InvestmentPot(value=pot_b_amount, name=name, risk=risk, type=type,interest_rate=interest)

        transfer = Money(value=10000, currency='£')
        success = pot_a.transfer(amount=transfer, to=pot_b)

        self.assertTrue(success)
        self.assertEqual(pot_a.total().total, pot_a_amount.subtract(other=transfer).total)

        self.assertEqual(pot_b.total().total, pot_b_amount.add(other=transfer).total)

    def test_transfer_respects_limits(self) -> None:

        name = 'pension'
        type = ''
        risk = 4

        pot_a_amount = Money(value=500, currency='£')
        interest = FixedSequence(0.1)

        pot_a = InvestmentPot(value=pot_a_amount, name=name, risk=risk, type=type,interest_rate=interest)

        name = 'pension'
        type = ''
        risk = 1

        pot_b_amount = Money(value=100000, currency='£')
        interest = FixedSequence(0.03)

        pot_b = InvestmentPot(value=pot_b_amount, name=name, risk=risk, type=type,interest_rate=interest)

        transfer = Money(value=10000, currency='£')
        success = pot_a.transfer(amount=transfer, to=pot_b)

        self.assertFalse(success)

        self.assertEqual(pot_a.total().total, pot_a_amount.total)

        self.assertEqual(pot_b.total().total, pot_b_amount.total)

    def test_transfer_can_empty_investment_pot(self) -> None:

        name = 'pension'
        type = ''
        risk = 4

        pot_a_amount = Money(value=500, currency='£')
        interest = FixedSequence(0.1)

        pot_a = InvestmentPot(value=pot_a_amount, name=name, risk=risk, type=type,interest_rate=interest)

        name = 'pension'
        type = ''
        risk = 1

        pot_b_amount = Money(value=100000, currency='£')
        interest = FixedSequence(0.03)

        pot_b = InvestmentPot(value=pot_b_amount, name=name, risk=risk, type=type,interest_rate=interest)

        transfer = Money(value=500, currency='£')
        success = pot_a.transfer(amount=transfer, to=pot_b)

        self.assertTrue(success)
        self.assertEqual(pot_a.total().total, 0)

        self.assertEqual(pot_b.total().total, 100500)
