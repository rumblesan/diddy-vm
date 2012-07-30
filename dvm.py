#!/usr/bin/env python

from vmbase import VMBase
# This is the class that contains all the instructions for the Diddy VM

class DVM(VMBase):

    # Language Instructions
    def move(self, A, B):
        pass

    def compare(self, A, B):
        pass

    def branch(self, A, B):
        pass

    def add(self, A, B):
        pass

    def subtract(self, A, B):
        pass


if __name__ == '__main__':
    import unittest
    from tests.testdvm import TestDVM
    unittest.main()

