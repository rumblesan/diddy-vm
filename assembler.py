#!/usr/bin/env python

import re
from argparse import ArgumentParser
from os.path import basename, splitext, join

lineParse = re.compile('^((?P<label>[a-zA-Z0-9]*): *| *)(?P<data>[a-zA-Z0-9]*)')


def parseArgs():
    parser = ArgumentParser(description='Assemble DiddyVM Program')
    parser.add_argument('program', help='The program to assemble')
    args = parser.parse_args()

    return args

def calculateLabels(programData):

    labels = {}
    num = 1
    for line in programData:
        label = lineParse.search(line).group('label')
        if label:
            labels[label] = num
        num += 1

    return labels


def assembleProgram(programData, labels):

    output = ""

    for line in programData:

        data = lineParse.search(line).group('data')

        if not line:
            output += "0\n"
        elif data in labels:
            output += str(labels[data]) + "\n"
        else:
            output += str(data) + "\n"

    return output

def main():

    args = parseArgs()

    inputFile = args.program
    fileName = basename(inputFile)
    outputName  = join('compiled', splitext(fileName)[0] + '.dcp')

    ofp = open(outputName, 'w')
    with open(inputFile) as ifp:
        programData = ifp.read().splitlines()

    labels = calculateLabels(programData)

    program = assembleProgram(programData, labels)

    ofp.write(program)

    ifp.close()
    ofp.close()

if __name__ == '__main__':
    main()

