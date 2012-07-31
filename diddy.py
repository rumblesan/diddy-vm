#!/usr/bin/env python

from dvm import DVM

from sys import argv

def main():
    dvm = DVM()

    program = argv[1]

    dvm.loadProgram(program)

    print("********")
    print("\n\n")

    while dvm.running == True:
        dvm.executeNextInstruction()

    print("\n\n")
    print("********")
    print("Finished")


if __name__ == '__main__':
    main()

