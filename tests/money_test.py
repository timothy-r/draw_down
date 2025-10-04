import unittest
from drawdown.source.money import Money

class MoneyTest(unittest.TestCase):

    def test_multiply_rounds_result(self)-> None:

        amount = 1000
        m = Money(amount=amount)
        percent = 1.0456
        result = m.multiply(value=percent)

        print(result)
        self.assertEqual(result, round(amount*percent,0))