#!/usr/bin/env python

from dvm import DVM

from sys import argv

def main():
    dvm = DVM()

    program = argv[1]

    dvm.loadProgram(program)

    dvm.run()


if __name__ == '__main__':
    main()

