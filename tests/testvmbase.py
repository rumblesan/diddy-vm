#!/usr/bin/env python

import unittest
from vmbase import VMBase

class TestVMBase(unittest.TestCase):

    def setUp(self):
        self.dvm = VMBase()

    def tearDown(self):
        del self.dvm

    def test_creation(self):
        self.assertIsInstance(self.dvm, VMBase)

    def testPushPop(self):
        self.dvm.push(1)
        self.dvm.push(2)
        self.dvm.push(3)
        self.assertEqual(self.dvm.pop(), 3)
        self.assertEqual(self.dvm.pop(), 2)
        self.assertEqual(self.dvm.pop(), 1)

    def testSetGetMem(self):
        self.dvm.setMem(1000, 1)
        self.dvm.setMem(2000, 2)
        self.dvm.setMem(3000, 3)
        self.assertEqual(self.dvm.getMem(1000), 1)
        self.assertEqual(self.dvm.getMem(2000), 2)
        self.assertEqual(self.dvm.getMem(3000), 3)

    def testHexToInt(self):
        self.assertEqual(self.dvm.hex2int('fff'), 4095)
        self.assertEqual(self.dvm.hex2int('0ff'), 255)
        self.assertEqual(self.dvm.hex2int('000'), 0)

    def testIntToHex(self):
        self.assertEqual(self.dvm.int2hex(4095), 'fff')
        self.assertEqual(self.dvm.int2hex(255), '0ff')
        self.assertEqual(self.dvm.int2hex(0), '000')

    def testSetAddrValue(self):
        self.dvm.setValue('*000', 123)
        self.dvm.setValue('*fff', 111)
        self.dvm.setValue('*b8a', 2954)
        self.assertEqual(self.dvm.getMem(0), 123)
        self.assertEqual(self.dvm.getMem(4095), 111)
        self.assertEqual(self.dvm.getMem(2954), 2954)

    def testGetAddrValue(self):
        self.dvm.setMem(0, 1)
        self.dvm.setMem(4095, 1111)
        self.dvm.setMem(3258, 555)
        self.assertEqual(self.dvm.getValue('*000'), 1)
        self.assertEqual(self.dvm.getValue('*fff'), 1111)
        self.assertEqual(self.dvm.getValue('*cba'), 555)

    def testSetStackValue(self):
        # Only first letter of address matters
        # Needs to be an 's' for stack operations
        self.dvm.setValue('stck', 123)
        self.dvm.setValue('stck', 111)
        self.dvm.setValue('stck', 2954)
        self.assertEqual(self.dvm.pop(), 2954)
        self.assertEqual(self.dvm.pop(), 111)
        self.assertEqual(self.dvm.pop(), 123)

    def testGetStackValue(self):
        # Only first letter of address matters
        # Needs to be an 's' for stack operations
        self.dvm.push(123)
        self.dvm.push(111)
        self.dvm.push(2954)
        self.assertEqual(self.dvm.getValue('stck'), 2954)
        self.assertEqual(self.dvm.getValue('stck'), 111)
        self.assertEqual(self.dvm.getValue('stck'), 123)

    def testGetLiteralValue(self):
        self.assertEqual(self.dvm.getValue('#fff'), 4095)
        self.assertEqual(self.dvm.getValue('#000'), 0)
        self.assertEqual(self.dvm.getValue('#cba'), 3258)

    def testGetSetValue(self):
        self.dvm.setValue('stck', 123)
        self.dvm.setValue('stck', 111)
        self.dvm.setValue('*bbb', 3003)
        self.dvm.setValue('*fff', 4095)
        self.assertEqual(self.dvm.getValue('stck'), 111)
        self.assertEqual(self.dvm.getValue('*bbb'), 3003)
        self.assertEqual(self.dvm.getValue('#aaa'), 2730)
        self.assertEqual(self.dvm.getValue('*fff'), 4095)
        self.assertEqual(self.dvm.getValue('stck'), 123)




