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

    def testPush(self):
        self.dvm.position = 1
        self.dvm.push(15)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.stack[0], 15)
        self.assertEqual(self.dvm.position, 2)
        self.dvm.setMem(4, 15)
        self.dvm.push((1 << 26) | 4)
        self.assertEqual(len(self.dvm.stack), 2)
        self.assertEqual(self.dvm.stack[1], 15)
        self.assertEqual(self.dvm.position, 3)

    def testPop(self):
        self.dvm.position = 1
        self.dvm.pushStack(1)
        self.dvm.pushStack(2)
        self.dvm.pushStack(3)
        self.dvm.pop(1)
        self.dvm.pop(2)
        self.dvm.pop(3)
        self.assertEqual(self.dvm.getMem(1), 3)
        self.assertEqual(self.dvm.getMem(2), 2)
        self.assertEqual(self.dvm.getMem(3), 1)
        self.assertEqual(self.dvm.position, 4)

    def testJump(self):
        self.dvm.position = 1
        self.dvm.jump(10)
        self.assertEqual(self.dvm.position, 10)
        self.dvm.pushStack(15)
        self.dvm.jump(1 << 26)
        self.assertEqual(self.dvm.position, 15)

    def testBranchTrueData(self):
        self.dvm.position = 1
        self.dvm.pushStack(1)
        self.dvm.branch(15)
        self.assertEqual(len(self.dvm.stack), 0)
        self.assertEqual(self.dvm.position, 15)

    def testBranchTrueStack(self):
        self.dvm.position = 1
        self.dvm.pushStack(10)
        self.dvm.pushStack(1)
        self.dvm.branch(1 << 26)
        self.assertEqual(len(self.dvm.stack), 0)
        self.assertEqual(self.dvm.position, 10)

    def testBranchFalse(self):
        self.dvm.position = 1
        self.dvm.pushStack(0)
        self.dvm.branch(15)
        self.assertEqual(len(self.dvm.stack), 0)
        self.assertEqual(self.dvm.position, 2)

    def testEqualTrue(self):
        self.dvm.position = 1
        self.dvm.pushStack(4)
        self.dvm.pushStack(4)
        self.dvm.equal(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testEqualFalse(self):
        self.dvm.position = 1
        self.dvm.pushStack(5)
        self.dvm.pushStack(4)
        self.dvm.equal(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 0)

    def testGreaterTrue(self):
        self.dvm.position = 1
        self.dvm.pushStack(5)
        self.dvm.pushStack(6)
        self.dvm.greater(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testGreaterFalse(self):
        self.dvm.position = 1
        self.dvm.pushStack(7)
        self.dvm.pushStack(6)
        self.dvm.greater(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 0)

    def testLesserTrue(self):
        self.dvm.position = 1
        self.dvm.pushStack(7)
        self.dvm.pushStack(6)
        self.dvm.lesser(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testLesserFalse(self):
        self.dvm.position = 1
        self.dvm.pushStack(5)
        self.dvm.pushStack(6)
        self.dvm.lesser(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 0)

    def testAdd(self):
        self.dvm.position = 1
        self.dvm.pushStack(5)
        self.dvm.pushStack(6)
        self.dvm.add(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 11)

    def testSubtractFalse(self):
        self.dvm.position = 1
        self.dvm.pushStack(5)
        self.dvm.pushStack(6)
        self.dvm.subtract(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testHaltStack(self):
        self.dvm.position = 1
        self.dvm.pushStack(5)
        self.assertEqual(self.dvm.status, 0)
        self.assertTrue(self.dvm.running)
        self.dvm.halt(0)
        self.assertFalse(self.dvm.running)
        self.assertEqual(self.dvm.status, 5)

    def testHaltData(self):
        self.dvm.position = 1
        self.assertEqual(self.dvm.status, 0)
        self.assertTrue(self.dvm.running)
        self.dvm.halt((1 << 26) | 5)
        self.assertFalse(self.dvm.running)
        self.assertEqual(self.dvm.status, 5)

