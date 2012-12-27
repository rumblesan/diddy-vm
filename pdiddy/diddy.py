#!/usr/bin/env python

from dvm import DVM

from argparse import ArgumentParser

from struct import unpack

def parseArgs():
    parser = ArgumentParser(description='DiddyVM')
    parser.add_argument('program', help='the program to run')
    parser.add_argument('-d', '--debug', help='enable debugging', action='store_true')
    parser.add_argument('-s', '--stack', help='enable stack display', action='store_true')

    return parser.parse_args()

def main():

    args = parseArgs()

    dvm = DVM(args.debug, args.stack)

    programData = []

    # The assembler writes the program to a file as binary data
    # stored as 4 byte integers. This reads the file, 4 bytes at
    # a time, converts it back to an integer, and then appends
    # it to an array.
    with open(args.program) as fp:
        for block in iter(lambda: fp.read(4), ""):
            value = unpack('@I', block)[0]
            programData.append(value)

    dvm.loadProgram(programData)

    while dvm.running == True:
        dvm.executeNextInstruction()

if __name__ == '__main__':
    main()

