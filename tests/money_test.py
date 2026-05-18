import unittest
from drawdown.source.money import Money

class MoneyTest(unittest.TestCase):

    def test_multiply_rounds_result(self)-> None:

        amount = 1000
        m = Money(value=amount, currency='£')

        percent = 1.0456
        result = m.multiply(value=percent)

        # print(result)
        self.assertIsInstance(result, Money)

        self.assertEqual(result.total, round(amount * percent, 0))

    def test_subtract(self) -> None:
        amount = 1000
        m = Money(value=amount, currency='£')

        sub = 500
        s = Money(value=sub, currency="£")

        result = m.subtract(other=s)

        self.assertIsInstance(result, Money)
        self.assertEqual(amount-sub, result.total)

    def test_subtract_does_not_create_negative_values(self) -> None:
        amount = 1000
        m = Money(value=amount, currency='£')

        sub = 5000
        s = Money(value=sub, currency="£")

        result = m.subtract(other=s)

        self.assertIsInstance(result, Money)
        self.assertEqual(0, result.total)

    def test_to_string(self) -> None:

        amount = 1000
        m = Money(value=amount, currency='£')

        expected = "£1,000.00"

        result = f"{m}"

        self.assertEqual(expected, result)