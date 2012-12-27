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

    def __init__(self, debug=False, stack_display=False):
        """
        The constructor of the VMBase parent class is called to set
        everything up, then the instructions dictionary is setup
        in this constructor
        """

        super(DVM, self).__init__(debug, stack_display)

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

        self.data_flag = 1 << 27
        self.pointer_flag = 1 << 26
        self.data_mask = ~(127 << 26)

    def nop(self, bits):
        """
        No Operation
        Just increments the position counter
        """
        if self.debug:
            print("Instruction:   NOP")
        self.next()

    # Data Movement Instructions
    def push(self, bits):
        """
        Push data onto the stack
        The data in the instruction is either the value
        to push onto the stack, or the address
        pointer to the value
        """
        if self.debug:
            print("Instruction:   PUSH")
        value = 0
        if bits & self.data_flag:
            value = bits & self.data_mask
        else:
            value = self.popStack()
        if bits & self.pointer_flag:
            value = self.getMem(value)
        self.pushStack(value)
        self.next()

    def pop(self, bits):
        """
        Pop the top value off the stack and load it into
        the memory location specified by the data value
        """
        if self.debug:
            print("Instruction:   POP")
        self.setMem(bits & self.data_mask, self.popStack())
        self.next()

    # Program Flow instructions
    def jump(self, bits):
        """
        Set the value of the instruction pointer
        Either to the data value, or to the top value
        of the stack, depending on the instruction flags
        """
        if self.debug:
            print("Instruction:   JUMP")
        value = 0
        if bits & self.data_flag:
            value = bits & self.data_mask
        else:
            value = self.popStack()
        if bits & self.pointer_flag:
            value = self.getMem(value)
        self.setInstructionPointer(value)

    def branch(self, bits):
        """
        Check the value ontop of the stack
        Jump the instruction pointer if it's not 0
        Set it to either the data value, or the next
        value on the stack, depending on the flags
        """
        if self.debug:
            print("Instruction:   BRANCH")
        if self.popStack():
            value = 0
            if bits & self.data_flag:
                value = bits & self.data_mask
            else:
                value = self.popStack()
            if bits & self.pointer_flag:
                value = self.getMem(value)
            self.setInstructionPointer(value)
        else:
            self.next()

    # Comparison instructions
    def equal(self, bits):
        """
        Compare the two values ontop of the stack
        If they're equal then push a 1 onto the stack
        Otherwise push a 0
        """
        if self.debug:
            print("Instruction:   EQUAL")

        aVal = self.popStack()
        if bits & self.data_flag:
            bVal = bits & self.data_mask
        else:
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
        if self.debug:
            print("Instruction:   GREATER")

        aVal = self.popStack()
        if bits & self.data_flag:
            bVal = bits & self.data_mask
        else:
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
        if self.debug:
            print("Instruction:   LESSER")

        aVal = self.popStack()
        if bits & self.data_flag:
            bVal = bits & self.data_mask
        else:
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
        if self.debug:
            print("Instruction:   ADD")

        aVal = self.popStack()
        if bits & self.data_flag:
            bVal = bits & self.data_mask
        else:
            bVal = self.popStack()
        self.pushStack(aVal + bVal)
        self.next()

    def subtract(self, bits):
        """
        Subtract the second value on the stack from
        the first then push the result back onto the stack
        """
        if self.debug:
            print("Instruction:   SUBTRACT")

        aVal = self.popStack()
        if bits & self.data_flag:
            bVal = bits & self.data_mask
        else:
            bVal = self.popStack()
        self.pushStack(aVal - bVal)
        self.next()

    def output(self, bits):
        """
        Write a value to the output
        Either the top value on the stack, or the data value
        depending on the flags
        """
        if self.debug:
            print("Instruction:   OUTPUT")

        if bits & self.data_flag:
            value = bits & self.data_mask
        else:
            value = self.popStack()
        if bits & self.pointer_flag:
            value = self.getMem(value)
        self.systemOut(value)
        self.next()

    def halt(self, bits):
        """
        Halt the program and set the exit status to the value at address A
        """
        if self.debug:
            print("Instruction:   HALT")

        if bits & self.data_flag:
            value = bits & self.data_mask
        else:
            value = self.popStack()
        if bits & self.pointer_flag:
            value = self.getMem(value)
        self.systemExit(value)

if __name__ == '__main__':
    import unittest
    from tests.testdvm import TestDVM
    unittest.main()

