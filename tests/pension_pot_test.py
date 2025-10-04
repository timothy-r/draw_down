import unittest

from drawdown.source.pension_pot import PensionPot

class PensionPotTest(unittest.TestCase):

    def test_withdraw_returns_deducted_value(self) -> None:

        amount = 500000
        pot = PensionPot(value=amount)

        deduction = 30000
        result = pot.withdraw(amount=deduction)

        self.assertEqual(deduction, result)

        total = pot.total()
        self.assertEqual(amount-deduction, total)

    def test_cannot_withdraw_more_than_total(self) -> None:

        amount = 10000
        pot = PensionPot(value=amount)

        deduction = 30000
        result = pot.withdraw(amount=deduction)

        self.assertEqual(amount, result)

        total = pot.total()
        self.assertEqual(0, total)

    def test_increase(self) -> None:
        amount = 10000
        pot = PensionPot(value=amount)

        percent = 0.1
        result = pot.increase(percent=percent)

        self.assertEqual(result, amount*percent)

        total = pot.total()
        self.assertEqual(result, total)

