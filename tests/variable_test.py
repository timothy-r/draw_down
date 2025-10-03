import unittest
import logging
import statistics

from drawdown.generate.variable import Variable

class VariableTest(unittest.TestCase):

    def test_min(self):

        average = 5.0
        min = 1.0
        max = 10.0
        period = 5

        var = Variable(average=average, min=min, max=max, period=period)

        next = var.next()
        # print(f"test_min {next}")
        self.assertGreaterEqual(next, min)

    def test_max(self):

        average = 5.0
        min = 1.0
        max = 10.0
        period = 5

        var = Variable(average=average, min=min, max=max, period=period)

        next = var.next()
        self.assertLessEqual(next, max)

    def test_average(self):

        min = 1.0
        max = 10.0
        average = round(statistics.mean([min,max]), 1)
        period = 5

        var = Variable(average=average, min=min, max=max, period=period)

        counter = 0
        vars = []

        while(counter < period):
            vars.append(var.next())
            counter +=1

        actual_average = round(statistics.mean(vars), 1)

        self.assertEqual(actual_average, average)