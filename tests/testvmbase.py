#!/usr/bin/env python

import unittest
from dvm import DVM

class TestVMBase(unittest.TestCase):

    def setUp(self):
        # Creating a DVM object but just testing the VMBase methods
        self.vmbase = DVM()

    def tearDown(self):
        del self.vmbase

    def test_creation(self):
        self.assertIsInstance(self.vmbase, DVM)

    def testSetInstructionPointer(self):
        self.vmbase.setInstructionPointer(100)
        self.assertEqual(self.vmbase.position, 100)

    def testNextInstructionPointer(self):
        self.vmbase.setInstructionPointer(100)
        self.vmbase.next()
        self.assertEqual(self.vmbase.position, 101)
        self.vmbase.next()
        self.assertEqual(self.vmbase.position, 102)

    def testSetMem(self):
        self.vmbase.setMem(100, 111)
        self.vmbase.setMem(101, 222)
        self.assertEqual(self.vmbase.ram[100], 111)
        self.assertEqual(self.vmbase.ram[101], 222)

    def testGetMem(self):
        self.vmbase.ram[200] = 200
        self.vmbase.ram[201] = 201
        self.assertEqual(self.vmbase.getMem(200), 200)
        self.assertEqual(self.vmbase.getMem(201), 201)

    def testGetPointerMem(self):
        self.vmbase.ram[200] = 200
        self.vmbase.ram[201] = 201
        self.vmbase.ram[202] = 202
        self.vmbase.setInstructionPointer(200)
        self.assertEqual(self.vmbase.getMem(), 200)
        self.vmbase.next()
        self.assertEqual(self.vmbase.getMem(), 201)
        self.vmbase.next()
        self.assertEqual(self.vmbase.getMem(), 202)

    def testSetGetMem(self):
        self.vmbase.setMem(200, 200)
        self.vmbase.setMem(201, 201)
        self.vmbase.setMem(202, 202)
        self.vmbase.setInstructionPointer(200)
        self.assertEqual(self.vmbase.getMem(), 200)
        self.vmbase.next()
        self.assertEqual(self.vmbase.getMem(), 201)
        self.vmbase.next()
        self.assertEqual(self.vmbase.getMem(), 202)
        self.assertEqual(self.vmbase.getMem(200), 200)
        self.assertEqual(self.vmbase.getMem(201), 201)
        self.assertEqual(self.vmbase.getMem(202), 202)


