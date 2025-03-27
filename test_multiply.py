#!/usr/bin/env python3

import unittest

from multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_basic(self):
        test_a = 5
        test_b = 6
        expected = 30
        self.assertEqual(multiply(test_a, test_b), (expected))

unittest.main()

