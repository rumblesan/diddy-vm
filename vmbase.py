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

    def __init__(self):
        self.ram = dict.fromkeys(xrange(2 ** 12), 0)
        self.instructions = {}

        self.position = 100

        self.registers = {}
        self.registers[0] = self.exit
        self.registers[1] = self.output

        self.setupInstructionTable()

        self.running = True
        self.status = 0

    # General purpose functions
    def executeNextInstruction(self):
        """
        Retrieves the value from the memory location pointed to
        by the position pointer and executes it
        """
        inst = self.ram[self.position]
        self.instructions[inst]()


    def setInstructionPointer(self, address):
        """
        Sets the instruction pointer to the specified address
        """
        self.position = address

    def next(self):
        self.position += 1

    def getMem(self, addr=-1):
        if addr == -1:
            output = self.ram[self.position]
        else:
            output = self.ram[addr]
        return output

    def setMem(self, addr, value):
        if addr in self.registers:
            self.registers[addr](value)
        else:
            self.ram[addr] = value

    def exit(self, value):
        """
        Set the running flag to false so the external program loop stops
        Also sets the exit status of the VM
        """
        self.running = False
        self.status = value

    def output(self, c):
        """
        Print a char to stdout
        """
        sys.stdout.write(chr(c))


    def loadProgram(self, filename):
        fp = open(filename)
        for line in fp:
            value = int(line)
            self.setMem(self.position, value)
            self.next()
        self.setInstructionPointer(100)



if __name__ == '__main__':
    import unittest
    from tests.testvmbase import TestVMBase
    unittest.main()

