"""
    test module
"""
import unittest

from tests.variable_sequence_test import VariableSequenceTest
from tests.fixed_sequence_test import FixedSequenceTest

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()

    runner.run(suite)