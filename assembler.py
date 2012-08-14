#!/usr/bin/env python

import re
from argparse import ArgumentParser
from os.path import basename, splitext, join

from struct import pack

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


def assembleProgram(programData, labels, instructions):

    output = []

    for line in programData:

        data = lineParse.search(line).group('data')

        if not line:
            output.append(0)
        elif data in labels:
            output.append(labels[data])
        elif data in instructions:
            output.append(instructions[data])
        else:
            output.append(int(data))

    return output

def setupInstructions():

    i = {}

    i['NOP'] =      0
    i['COPY'] =     1
    i['JUMP'] =     2
    i['BRANCH'] =   3
    i['EQUAL'] =    4
    i['GREATER'] =  5
    i['LESSER'] =   6
    i['ADD'] =      7
    i['SUBTRACT'] = 8
    i['OUTPUT'] =   9
    i['HALT'] =     10

    return i


def main():

    args = parseArgs()

    inputFile = args.program
    fileName = basename(inputFile)
    outputName  = join('compiled', splitext(fileName)[0] + '.dcp')

    ofp = open(outputName, 'w')
    with open(inputFile) as ifp:
        programData = ifp.read().splitlines()

    instructions = setupInstructions()

    labels = calculateLabels(programData)

    program = assembleProgram(programData, labels, instructions)

    for datum in program:
        ofp.write(pack('@I', datum))

    ifp.close()
    ofp.close()

if __name__ == '__main__':
    main()

