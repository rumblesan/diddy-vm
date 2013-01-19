#!/usr/bin/env python

# This is the class that contains all the basic methods for the Diddy VM
#
# This machine operates entirely in RAM
# There are registers for special uses,
#   Input
#   Output
#   Exiting
# Instructions can have a variable number of arguments
# The machines memory width is 16 bits

import sys


class VMBase(object):

    """
    The base VM class
    Contains the internal data structures as well as general purpose methods

    A VM Class with the instruction methods should inherit this
    """

    def __init__(self, debug=False, stack_display=False):
        """
        Setup the ram, instruction dictionary and register dictionary
        """
        self.ram = dict.fromkeys(xrange(2 ** 12), 0)
        self.instructions = {}

        self.position = 1

        self.running = True
        self.status = 0

        self.stack = []

        self.debug = debug
        self.stack_display = stack_display

        self.instruction_mask = 31 << 28

    # General purpose functions
    def executeNextInstruction(self):
        """
        Retrieves the value from the memory location pointed to
        by the position pointer and executes it
        """
        bits = self.ram[self.position]
        inst = (bits & self.instruction_mask) >> 28

        self.instructions[inst](bits)

    def setInstructionPointer(self, address):
        """
        Sets the instruction pointer to the specified address
        """
        self.position = address

    def next(self):
        """
        Increments program position counter
        """
        self.position += 1

    def pushStack(self, data):
        """
        Push a value onto the VM stack
        data should be an integer
        """
        value = self.stack.append(data)
        if self.debug:
            print("stack size:  %i" % len(self.stack))
        if self.stack_display:
            print(self.stack)
        return value

    def popStack(self):
        """
        Pop a value off the VM stack
        data should be an integer
        """
        try:
            value = self.stack.pop()
            if self.debug:
                print("stack size:  %i" % len(self.stack))
            if self.stack_display:
                print(self.stack)
            return value
        except IndexError:
            self.systemExit(1)

    def getMem(self, addr=-1):
        """
        Retrieve a value from a memory address
        If no address is given then the value from the
        position pointer will be retrieved
        """
        if addr == -1:
            output = self.ram[self.position]
        else:
            output = self.ram[addr]
        return output

    def setMem(self, addr, value):
        """
        Set a value in memory
        If the memory position corresponds to a register then
        the register function will be called instead
        """
        self.ram[addr] = value

    def systemExit(self, value):
        """
        Set the running flag to false so the external program loop stops
        Also sets the exit status of the VM
        """
        self.running = False
        self.status = value

    def systemOut(self, c):
        """
        Print a char to stdout
        """
        sys.stdout.write(chr(c))

    def loadProgram(self, programData):
        """
        Loads a program into memory
        The programdata should be a list of integers
        """
        for value in programData:
            self.setMem(self.position, value)
            self.next()
        self.setInstructionPointer(1)

if __name__ == '__main__':
    import unittest
    from tests.testvmbase import TestVMBase
    unittest.main()
