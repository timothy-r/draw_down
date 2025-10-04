import unittest

from drawdown.generate.fixed_sequence import FixedSequence

class FixedSequenceTest(unittest.TestCase):

    def test_sequence(self)-> None:

        value = 4.5
        seq = FixedSequence(value=value)

        result = seq.next()

        self.assertEqual(value, result)