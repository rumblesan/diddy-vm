#!/usr/bin/env python

# This is the class that contains all the logic for the Diddy VM
# The VM has two sections, the RAM and the Stack
# I probablly only need one or the other of these
# but right now I don't know what I'm doing so just roll with it

class VMBase(object):

    def __init__(self):
        self.ram = dict.fromkeys(xrange(2 ** 12), 0)
        self.stack = []
        self.position = 0

    # General purpose functions
    def executeNextInstruction(self):
        pass

    def getValue(self, addr):
        """
        Retrieves a value based on the input
        Address values are always 4 characters and correspond to RAM
        addresses, literal values or the top value popped off the stack

        Addresses in RAM are prefixed by a *
            e.g.  *00F corresponds to the 16th position in RAM

        Literal values are prefixed with a #
            e.g.  #F50 is a value of 3920

        Stack values are prefixed with an 's', the remaining
        three chars don't matter. The value returned will be
        the next value popped off the stack
        """
        t = addr[0]
        pos = addr[1:]
        if t == '*':
            memAddr = self.hex2int(pos)
            output = self.getMem(memAddr)
        elif t == '#':
            output = self.hex2int(pos)
        elif t == 's':
            output = self.pop()
        return output

    def setValue(self, addr, val):
        """
        Sets the value in the correct structure. Either stack or RAM
        Address values are always 4 characters and correspond to RAM
        addresses or a command to push the value to the stack

        Addresses in RAM are prefixed by a *
            e.g.  *00F corresponds to the 16th position in RAM

        Stack values are prefixed with an 's', the remaining
        three chars don't matter. The value is pushed onto the stack
        """
        t = addr[0]
        pos = addr[1:]
        if t == '*':
            memAddr = self.hex2int(pos)
            self.setMem(memAddr, val)
        elif t == '#':
            pass
        elif t == 's':
            self.push(val)

    def setMem(self, addr, val):
        self.ram[addr] = val

    def getMem(self, addr):
        return self.ram[addr]

    def push(self, v):
        self.stack.append(v)

    def pop(self):
        return self.stack.pop()

    def hex2int(self, val):
        return int(val, 16)

    def int2hex(self, val):
        return hex(val)[2:].rjust(3, '0')



if __name__ == '__main__':
    import unittest
    from tests.testvmbase import TestVMBase
    unittest.main()

