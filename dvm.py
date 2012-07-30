#!/usr/bin/env python

from vmbase import VMBase
# This is the class that contains all the instructions for the Diddy VM

class DVM(VMBase):

    def setupInstructionTable(self):
        self.instructions = {}

        i = self.instructions

        i['move'] = self.move
        i['jump'] = self.jump
        i['brch'] = self.branch
        i['eqal'] = self.equal
        i['grtr'] = self.greater
        i['lssr'] = self.lesser
        i['addd'] = self.add
        i['subb'] = self.subtract

    # Data Movement Instructions
    def move(self, A, B):
        """
        Move data from one place to another
        """
        inVal = self.getValue(A)
        self.setValue(B, inVal)

    # Program Flow instructions
    def jump(self, A, B):
        """
        Set the next instruction pointer to be A
        B is unused
        """
        self.setInstructionPointer(A)

    def branch(self, A, B):
        """
        Pop the top value off the stack
        Set the next instruction pointer to be B if it's 0
        set it to A otherwise
        """
        testVal = self.pop()
        if testVal == 0:
            self.setInstructionPointer(B)
        else:
            self.setInstructionPointer(A)

    # Comparison instructions
    def equal(self, A, B):
        """
        Compare two values for equality
        Push a 1 to the stack if they're the same, 0 otherwise
        """
        aVal = self.getValue(A)
        bVal = self.getValue(B)
        if aVal == bVal:
            self.push(1)
        else:
            self.push(0)

    def greater(self, A, B):
        """
        Push a 1 to the stack if A > B, 0 otherwise
        """
        aVal = self.getValue(A)
        bVal = self.getValue(B)
        if aVal > bVal:
            self.push(1)
        else:
            self.push(0)

    def lesser(self, A, B):
        """
        Push a 1 to the stack if A < B, 0 otherwise
        """
        aVal = self.getValue(A)
        bVal = self.getValue(B)
        if aVal < bVal:
            self.push(1)
        else:
            self.push(0)

    # Manipulation Instructions
    def add(self, A, B):
        """
        Add A to B and push the result to the stack
        At some point this will have max values for integer operations.
        """
        aVal = self.getValue(A)
        bVal = self.getValue(B)
        self.push(aVal + bVal)

    def subtract(self, A, B):
        """
        Subtract B from A and push the result to the stack
        At some point this will have min values for integer operations.
        """
        aVal = self.getValue(A)
        bVal = self.getValue(B)
        self.push(aVal - bVal)


if __name__ == '__main__':
    import unittest
    from tests.testdvm import TestDVM
    unittest.main()

