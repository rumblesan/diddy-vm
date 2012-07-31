#!/usr/bin/env python

from vmbase import VMBase
# This is the class that contains all the instructions for the Diddy VM

class DVM(VMBase):

    def __init__(self):

        super(DVM, self).__init__()

        i = self.instructions

        i[0] = self.nop
        i[1] = self.copy
        i[2] = self.jump
        i[3] = self.branch
        i[4] = self.equal
        i[5] = self.greater
        i[6] = self.lesser
        i[7] = self.add
        i[8] = self.subtract
        i[9] = self.output
        i[10] = self.halt

    def nop(self):
        """
        No Operation
        Just increments the position counter
        """
        self.next()

    # Data Movement Instructions
    def copy(self):
        """
        Copy data at position A to position B
        """
        self.next()
        inAddr = self.getMem()
        inVal = self.getMem(inAddr)
        self.next()
        outAddr = self.getMem()
        self.setMem(outAddr, inVal)
        self.next()

    # Program Flow instructions
    def jump(self):
        """
        Set the next instruction pointer to the value pointed to by A
        """
        self.next()
        inAddr = self.getMem()
        self.setInstructionPointer(inAddr)

    def branch(self):
        """
        Check the value at address A
        Set the next instruction pointer to be C if it's 0
        set it to B otherwise
        """
        self.next()
        aAddr = self.getMem()
        aVal = self.getMem(aAddr)

        self.next()
        bAddr = self.getMem()

        self.next()
        cAddr = self.getMem()

        if aVal == 0:
            self.setInstructionPointer(cAddr)
        else:
            self.setInstructionPointer(bAddr)


    # Comparison instructions
    def equal(self):
        """
        Compare two values for equality
        Write a 1 to address C if the values at address A and B
        are equal, otherwise write a 0
        """
        self.next()
        aAddr = self.getMem()
        aVal = self.getMem(aAddr)

        self.next()
        bAddr = self.getMem()
        bVal = self.getMem(bAddr)

        self.next()
        cAddr = self.getMem()

        if aVal == bVal:
            self.setMem(cAddr, 1)
        else:
            self.setMem(cAddr, 0)

        self.next()

    def greater(self):
        """
        Compare two values
        Write a 1 to address C if the value at address A
        is greater than that at address B, otherwise write a 0
        """
        self.next()
        aAddr = self.getMem()
        aVal = self.getMem(aAddr)

        self.next()
        bAddr = self.getMem()
        bVal = self.getMem(bAddr)

        self.next()
        cAddr = self.getMem()

        if aVal > bVal:
            self.setMem(cAddr, 1)
        else:
            self.setMem(cAddr, 0)

        self.next()

    def lesser(self):
        """
        Compare two values
        Write a 1 to address C if the value at address A
        is less than that at address B, otherwise write a 0
        """
        self.next()
        aAddr = self.getMem()
        aVal = self.getMem(aAddr)

        self.next()
        bAddr = self.getMem()
        bVal = self.getMem(bAddr)

        self.next()
        cAddr = self.getMem()

        if aVal < bVal:
            self.setMem(cAddr, 1)
        else:
            self.setMem(cAddr, 0)

        self.next()


    # Manipulation Instructions
    def add(self):
        """
        Add values at addresses A and B then write it to address pointed to by C
        """
        self.next()
        aAddr = self.getMem()
        aVal = self.getMem(aAddr)

        self.next()
        bAddr = self.getMem()
        bVal = self.getMem(bAddr)

        self.next()
        cAddr = self.getMem()

        value = aVal + bVal

        self.setMem(cAddr, value)

        self.next()

    def subtract(self):
        """
        Subtract value at addresses B from A then write it to address pointed to by C
        """
        self.next()
        aAddr = self.getMem()
        aVal = self.getMem(aAddr)

        self.next()
        bAddr = self.getMem()
        bVal = self.getMem(bAddr)

        self.next()
        cAddr = self.getMem()

        value = aVal - bVal

        self.setMem(cAddr, value)

        self.next()

    def output(self):
        """
        Write the value at address A to the output
        """
        self.next()
        aAddr = self.getMem()
        aVal = self.getMem(aAddr)
        self.systemOut(aVal)
        self.next()

    def halt(self):
        """
        Halt the program
        """
        self.next()
        aAddr = self.getMem()
        aVal = self.getMem(aAddr)
        self.systemExit(aVal)

if __name__ == '__main__':
    import unittest
    from tests.testdvm import TestDVM
    unittest.main()

