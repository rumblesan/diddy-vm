#!/usr/bin/env python

from dvm import DVM

from sys import argv

def main():
    dvm = DVM()

    program = argv[1]

    programData = open(program).read().splitlines()

    dvm.loadProgram(programData)

    while dvm.running == True:
        dvm.executeNextInstruction()


if __name__ == '__main__':
    main()

