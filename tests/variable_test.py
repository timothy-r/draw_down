import unittest
from drawdown.generate.variable import Variable

class VariableTest(unittest.TestCase):

    def test_min(self):

        average = 5.0
        min = 1.0
        max = 10.0
        period = 5

        var = Variable(average=average, min=min, max=max, period=period)

        next = var.next()
        self.assertGreaterEqual(min, next)