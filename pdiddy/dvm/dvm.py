#!/usr/bin/env python

from vmbase import VMBase
# This is the class that contains all the instructions for the Diddy VM

class DVM(VMBase):
    """
    This contains the methods for each of the VM instructions

        * NOP
        * Copy
        * Jump
        * Branch
        * Equal
        * Greater Than
        * Less Than
        * Add
        * Subtract
        * Output
        * Halt
    """

    def __init__(self):
        """
        The constructor of the VMBase parent class is called to set
        everything up, then the instructions dictionary is setup
        in this constructor
        """

        super(DVM, self).__init__()

        i = self.instructions

        i[0 << 28] = self.nop
        i[1 << 28] = self.push
        i[2 << 28] = self.pop
        i[3 << 28] = self.jump
        i[4 << 28] = self.branch
        i[5 << 28] = self.equal
        i[6 << 28] = self.greater
        i[7 << 28] = self.lesser
        i[8 << 28] = self.add
        i[9 << 28] = self.subtract
        i[10 << 28] = self.output
        i[11 << 28] = self.halt

    def nop(self):
        """
        No Operation
        Just increments the position counter
        """
        self.next()

    # Data Movement Instructions
    def push(self, bits):
        """
        Push data onto the stack
        The data in the instruction is either the value
        to push onto the stack, or the address
        pointer to the value
        """
        flags = (bits & self.flag_mask) >> 26
        data = bits & self.data_mask
        if flags == 0:
            self.pushStack(data)
        elif flags == 1:
            self.pushStack(self.getMem(data))
        self.next()

    def pop(self, bits):
        """
        Pop the top value off the stack and load it into
        the memory location specified by the data value
        """
        self.setMem(bits & self.data_mask, self.popStack())
        self.next()

    # Program Flow instructions
    def jump(self, bits):
        """
        Set the value of the instruction pointer
        Either to the data value, or to the top value
        of the stack, depending on the instruction flags
        """
        flags = (bits & self.flag_mask) >> 26
        data = bits & self.data_mask
        if flags == 0:
            self.setInstructionPointer(data)
        elif flags == 1:
            self.setInstructionPointer(self.popStack())

    def branch(self, bits):
        """
        Check the value ontop of the stack
        Jump the instruction pointer if it's not 0
        Set it to either the data value, or the next
        value on the stack, depending on the flags
        """
        flags = (bits & self.flag_mask) >> 26
        data = bits & self.data_mask
        test = self.popStack()
        if test != 0:
            if flags == 0:
                self.setInstructionPointer(data)
            elif flags == 1:
                self.setInstructionPointer(self.popStack())
        else:
            self.next()

    # Comparison instructions
    def equal(self, bits):
        """
        Compare the two values ontop of the stack
        If they're equal then push a 1 onto the stack
        Otherwise push a 0
        """
        aVal = self.popStack()
        bVal = self.popStack()

        if aVal == bVal:
            self.pushStack(1)
        else:
            self.pushStack(0)

        self.next()

    def greater(self, bits):
        """
        Compare two values ontop of the stack
        Push a 1 onto the stack if the first value
        is greater than the second, otherwise write a 0
        """
        aVal = self.popStack()
        bVal = self.popStack()

        if aVal > bVal:
            self.pushStack(1)
        else:
            self.pushStack(0)

        self.next()

    def lesser(self, bits):
        """
        Compare two values ontop of the stack
        Push a 1 onto the stack if the first value
        is less than the second, otherwise write a 0
        """
        aVal = self.popStack()
        bVal = self.popStack()

        if aVal < bVal:
            self.pushStack(1)
        else:
            self.pushStack(0)

        self.next()

    # Manipulation Instructions
    def add(self, bits):
        """
        Add the top two values on the stack then push
        the result back onto the stack
        """
        aVal = self.popStack()
        bVal = self.popStack()
        self.pushStack(aVal + bVal)
        self.next()

    def subtract(self, bits):
        """
        Subtract the second value on the stack from
        the first then push the result back onto the stack
        """
        aVal = self.popStack()
        bVal = self.popStack()
        self.pushStack(aVal - bVal)
        self.next()

    def output(self, bits):
        """
        Write a value to the output
        Either the top value on the stack, or the data value
        depending on the flags
        """
        flags = (bits & self.flag_mask) >> 26
        data = bits & self.data_mask
        if flags == 0:
            self.systemOut(data)
        elif flags == 1:
            self.systemOut(self.popStack())
        self.next()

    def halt(self, bits):
        """
        Halt the program and set the exit status to the value at address A
        """
        flags = (bits & self.flag_mask) >> 26
        data = bits & self.data_mask
        if flags == 0:
            self.systemExit(data)
        elif flags == 1:
            self.systemExit(self.popStack())

if __name__ == '__main__':
    import unittest
    from tests.testdvm import TestDVM
    unittest.main()

