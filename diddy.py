#!/usr/bin/env python

from dvm import DVM

from sys import argv
from struct import unpack

def main():
    dvm = DVM()

    program = argv[1]

    programData = []

    # The assembler writes the program to a file as binary data
    # stored as 4 byte integers. This reads the file, 4 bytes at
    # a time, converts it back to an integer, and then appends
    # it to an array.
    with open(program) as fp:
        for block in iter(lambda: fp.read(4), ""):
            value = unpack('@I', block)[0]
            programData.append(value)


    dvm.loadProgram(programData)

    while dvm.running == True:
        dvm.executeNextInstruction()


if __name__ == '__main__':
    main()

