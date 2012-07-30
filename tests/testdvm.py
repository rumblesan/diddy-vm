#!/usr/bin/env python

import unittest
from dvm import DVM

class TestDVM(unittest.TestCase):

    def setUp(self):
        self.dvm = DVM()

    def tearDown(self):
        del self.dvm

    def test_creation(self):
        self.assertIsInstance(self.dvm, DVM)


