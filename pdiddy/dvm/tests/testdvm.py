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
        self.assertEqual(self.dvm.position, 1)

    def testNop(self):
        self.dvm.nop(0)
        self.assertEqual(self.dvm.position, 2)

    def testPushData(self):
        self.dvm.push(self.dvm.data_flag | 10)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.stack[0], 10)
        self.assertEqual(self.dvm.position, 2)

    def testPushStack(self):
        self.dvm.push(self.dvm.data_flag | 10)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.stack[0], 10)
        self.dvm.push(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.stack[0], 10)
        self.assertEqual(self.dvm.position, 3)

    def testPushPointer(self):
        self.dvm.setMem(4, 15)
        self.dvm.push(self.dvm.data_flag | self.dvm.pointer_flag | 4)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.stack[0], 15)
        self.assertEqual(self.dvm.position, 2)

    def testPop(self):
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

    def testJumpData(self):
        self.dvm.jump(self.dvm.data_flag | 10)
        self.assertEqual(self.dvm.position, 10)

    def testJumpStack(self):
        self.dvm.pushStack(15)
        self.assertEqual(len(self.dvm.stack), 1)
        self.dvm.jump(0)
        self.assertEqual(len(self.dvm.stack), 0)
        self.assertEqual(self.dvm.position, 15)

    def testJumpPointer(self):
        self.dvm.setMem(4, 10)
        self.dvm.pushStack(4)
        self.dvm.jump(self.dvm.pointer_flag)
        self.assertEqual(self.dvm.position, 10)

    def testBranchTrueData(self):
        self.dvm.pushStack(1)
        self.dvm.branch(self.dvm.data_flag | 15)
        self.assertEqual(len(self.dvm.stack), 0)
        self.assertEqual(self.dvm.position, 15)

    def testBranchTrueStack(self):
        self.dvm.pushStack(10)
        self.dvm.pushStack(1)
        self.dvm.branch(0)
        self.assertEqual(len(self.dvm.stack), 0)
        self.assertEqual(self.dvm.position, 10)

    def testBranchTrueDataPointer(self):
        self.dvm.pushStack(1)
        self.dvm.setMem(15, 10)
        self.dvm.branch(self.dvm.pointer_flag | self.dvm.data_flag | 15)
        self.assertEqual(len(self.dvm.stack), 0)
        self.assertEqual(self.dvm.position, 10)

    def testBranchTrueStackPointer(self):
        self.dvm.pushStack(15)
        self.dvm.pushStack(1)
        self.dvm.setMem(15, 10)
        self.dvm.branch(self.dvm.pointer_flag | 0)
        self.assertEqual(len(self.dvm.stack), 0)
        self.assertEqual(self.dvm.position, 10)

    def testBranchFalse(self):
        self.dvm.pushStack(0)
        self.dvm.branch(15)
        self.assertEqual(len(self.dvm.stack), 0)
        self.assertEqual(self.dvm.position, 2)

    def testEqualDataTrue(self):
        self.dvm.pushStack(4)
        self.dvm.equal(self.dvm.data_flag | 4)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testEqualStackTrue(self):
        self.dvm.pushStack(4)
        self.dvm.pushStack(4)
        self.dvm.equal(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testEqualDataFalse(self):
        self.dvm.pushStack(5)
        self.dvm.equal(self.dvm.data_flag | 4)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 0)

    def testEqualStackFalse(self):
        self.dvm.pushStack(5)
        self.dvm.pushStack(4)
        self.dvm.equal(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 0)

    def testGreaterDataTrue(self):
        self.dvm.pushStack(5)
        self.dvm.greater(self.dvm.data_flag | 4)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testGreaterStackTrue(self):
        self.dvm.pushStack(5)
        self.dvm.pushStack(6)
        self.dvm.greater(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testGreaterDataFalse(self):
        self.dvm.pushStack(7)
        self.dvm.greater(self.dvm.data_flag | 8)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 0)

    def testGreaterStackFalse(self):
        self.dvm.pushStack(7)
        self.dvm.pushStack(6)
        self.dvm.greater(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 0)

    def testLesserDataTrue(self):
        self.dvm.pushStack(7)
        self.dvm.lesser(self.dvm.data_flag | 8)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testLesserStackTrue(self):
        self.dvm.pushStack(7)
        self.dvm.pushStack(6)
        self.dvm.lesser(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testLesserDataFalse(self):
        self.dvm.pushStack(5)
        self.dvm.lesser(self.dvm.data_flag | 4)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 0)

    def testLesserStackFalse(self):
        self.dvm.pushStack(5)
        self.dvm.pushStack(6)
        self.dvm.lesser(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 0)

    def testAddData(self):
        self.dvm.pushStack(5)
        self.dvm.add(self.dvm.data_flag | 6)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 11)

    def testAddStack(self):
        self.dvm.pushStack(5)
        self.dvm.pushStack(6)
        self.dvm.add(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 11)

    def testSubtractData(self):
        self.dvm.pushStack(5)
        self.dvm.subtract(self.dvm.data_flag | 4)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testSubtractStack(self):
        self.dvm.pushStack(5)
        self.dvm.pushStack(6)
        self.dvm.subtract(0)
        self.assertEqual(len(self.dvm.stack), 1)
        self.assertEqual(self.dvm.position, 2)
        self.assertEqual(self.dvm.stack[0], 1)

    def testHaltStack(self):
        self.dvm.pushStack(5)
        self.assertEqual(self.dvm.status, 0)
        self.assertTrue(self.dvm.running)
        self.dvm.halt(5)
        self.assertEqual(self.dvm.status, 5)
        self.assertFalse(self.dvm.running)

    def testHaltData(self):
        self.assertEqual(self.dvm.status, 0)
        self.assertTrue(self.dvm.running)
        self.dvm.halt(self.dvm.data_flag | 5)
        self.assertEqual(self.dvm.status, 5)
        self.assertFalse(self.dvm.running)

    def testHaltDataPointer(self):
        self.dvm.pushStack(10)
        self.assertEqual(self.dvm.status, 0)
        self.assertTrue(self.dvm.running)
        self.dvm.setMem(10, 5)
        self.dvm.halt(self.dvm.pointer_flag | 10)
        self.assertEqual(self.dvm.status, 5)
        self.assertFalse(self.dvm.running)

    def testHaltStackPointer(self):
        self.assertEqual(self.dvm.status, 0)
        self.assertTrue(self.dvm.running)
        self.dvm.setMem(10, 5)
        self.dvm.halt(self.dvm.pointer_flag | self.dvm.data_flag | 10)
        self.assertEqual(self.dvm.status, 5)
        self.assertFalse(self.dvm.running)

