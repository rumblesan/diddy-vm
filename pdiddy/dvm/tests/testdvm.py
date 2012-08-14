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

    def testNop(self):
        self.dvm.position = 1
        self.dvm.nop()
        self.assertEqual(self.dvm.position, 2)

    def testCopy(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 4)
        self.dvm.setMem(3, 5)
        self.dvm.setMem(4, 9)
        self.dvm.setMem(5, 8)
        self.assertEqual(self.dvm.getMem(4), 9)
        self.assertEqual(self.dvm.getMem(5), 8)
        self.dvm.copy()
        self.assertEqual(self.dvm.getMem(4), 9)
        self.assertEqual(self.dvm.getMem(5), 9)

    def testJump(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.jump()
        self.assertEqual(self.dvm.position, 5)

    def testBranchTrue(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.setMem(3, 5)
        self.dvm.setMem(4, 6)
        self.dvm.setMem(5, 1)
        self.assertEqual(self.dvm.position, 1)
        self.dvm.branch()
        self.assertEqual(self.dvm.position, 5)

    def testBranchFalse(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.setMem(3, 5)
        self.dvm.setMem(4, 6)
        self.dvm.setMem(5, 0)
        self.assertEqual(self.dvm.position, 1)
        self.dvm.branch()
        self.assertEqual(self.dvm.position, 6)

    def testEqualTrue(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.setMem(3, 6)
        self.dvm.setMem(4, 7)
        self.dvm.setMem(5, 0)
        self.dvm.setMem(6, 0)
        self.dvm.setMem(7, 4)
        self.assertEqual(self.dvm.getMem(7), 4)
        self.dvm.equal()
        self.assertEqual(self.dvm.getMem(7), 1)

    def testEqualFalse(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.setMem(3, 6)
        self.dvm.setMem(4, 7)
        self.dvm.setMem(5, 0)
        self.dvm.setMem(6, 1)
        self.dvm.setMem(7, 4)
        self.assertEqual(self.dvm.getMem(7), 4)
        self.dvm.equal()
        self.assertEqual(self.dvm.getMem(7), 0)

    def testGreaterTrue(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.setMem(3, 6)
        self.dvm.setMem(4, 7)
        self.dvm.setMem(5, 1)
        self.dvm.setMem(6, 0)
        self.dvm.setMem(7, 4)
        self.assertEqual(self.dvm.getMem(7), 4)
        self.dvm.greater()
        self.assertEqual(self.dvm.getMem(7), 1)

    def testGreaterFalse(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.setMem(3, 6)
        self.dvm.setMem(4, 7)
        self.dvm.setMem(5, 0)
        self.dvm.setMem(6, 1)
        self.dvm.setMem(7, 4)
        self.assertEqual(self.dvm.getMem(7), 4)
        self.dvm.greater()
        self.assertEqual(self.dvm.getMem(7), 0)

    def testLesserTrue(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.setMem(3, 6)
        self.dvm.setMem(4, 7)
        self.dvm.setMem(5, 0)
        self.dvm.setMem(6, 1)
        self.dvm.setMem(7, 4)
        self.assertEqual(self.dvm.getMem(7), 4)
        self.dvm.lesser()
        self.assertEqual(self.dvm.getMem(7), 1)

    def testLesserFalse(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.setMem(3, 6)
        self.dvm.setMem(4, 7)
        self.dvm.setMem(5, 1)
        self.dvm.setMem(6, 0)
        self.dvm.setMem(7, 4)
        self.assertEqual(self.dvm.getMem(7), 4)
        self.dvm.lesser()
        self.assertEqual(self.dvm.getMem(7), 0)

    def testAdd(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.setMem(3, 6)
        self.dvm.setMem(4, 7)
        self.dvm.setMem(5, 9)
        self.dvm.setMem(6, 7)
        self.dvm.setMem(7, 4)
        self.assertEqual(self.dvm.getMem(7), 4)
        self.dvm.add()
        self.assertEqual(self.dvm.getMem(7), 16)

    def testSubtractFalse(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 5)
        self.dvm.setMem(3, 6)
        self.dvm.setMem(4, 7)
        self.dvm.setMem(5, 9)
        self.dvm.setMem(6, 4)
        self.dvm.setMem(7, 4)
        self.assertEqual(self.dvm.getMem(7), 4)
        self.dvm.subtract()
        self.assertEqual(self.dvm.getMem(7), 5)

    def testHalt(self):
        self.dvm.position = 1
        self.dvm.setMem(2, 3)
        self.dvm.setMem(3, 5)
        self.assertEqual(self.dvm.status, 0)
        self.assertTrue(self.dvm.running)
        self.dvm.halt()
        self.assertFalse(self.dvm.running)
        self.assertEqual(self.dvm.status, 5)





