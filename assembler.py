#!/usr/bin/env python

import re
from argparse import ArgumentParser
from os.path import basename, splitext, join

def parseArgs():
    parser = ArgumentParser(description='Assemble DiddyVM Program')
    parser.add_argument('program', help='The program to assemble')
    args = parser.parse_args()

    return args



def assembleProgram(programData, output):

    strip = re.compile('(^[a-zA-Z0-9]*)')

    for l in programData:

        l = strip.search(l).group(1)

        # If this is an address, remove the A at the front
        if not l:
            output.write("0\n")
        elif l[0] == "A":
            val = int(l[1:])
            output.write(str(val) + "\n")
        else:
            output.write(l + "\n")



def main():

    args = parseArgs()

    inputFile = args.program
    fileName = basename(inputFile)
    outputName  = join('compiled', splitext(fileName)[0] + '.dcp')

    ofp = open(outputName, 'w')

    with open(inputFile) as ifp:
        programData = ifp.read().splitlines()
        assembleProgram(programData, ofp)

    ifp.close()
    ofp.close()

if __name__ == '__main__':
    main()

