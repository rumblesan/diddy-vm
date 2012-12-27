#!/usr/bin/env python

import re
from argparse import ArgumentParser
from os.path import basename, splitext, join

from struct import pack

labelParse = re.compile('^(?P<label>[a-z0-9]+):')
lineParse = re.compile('^(?:[a-z0-9]*:)? *(((?P<pflag>\*)?(?P<dflag>#)?(?P<inst>[A-Z]+)( *(?P<pointer>[a-z0-9]+))?)|(?P<data>[a-zA-Z0-9]+))')


def parseArgs():
    parser = ArgumentParser(description='Assemble DiddyVM Program')
    parser.add_argument('program', help='The program to assemble')
    args = parser.parse_args()

    return args

def calculateLabels(programData):

    labels = {}
    num = 1
    for line in programData:
        label = labelParse.search(line)
        if label:
            l = label.group('label')
            labels[l] = num
        num += 1

    return labels


def assembleProgram(programData, labels, instructions):

    output = []

    for line in programData:

        data = lineParse.search(line)

        if not line:
            output.append(0)
        elif data.group('data'):
            d = data.group('data')
            if d in labels:
                output.append(labels[d])
            else:
                output.append(int(d))
        elif data.group('inst'):
            v = instructions[data.group('inst')]
            if data.group('dflag'):
                v = v | (1 << 27)
            if data.group('pflag'):
                v = v | (1 << 26)
            if data.group('pointer'):
                p = data.group('pointer')
                if p in labels:
                    v = v | labels[p]
                else:
                    v = v | int(p)
            output.append(v)

    return output

def setupInstructions():

    i = {}

    i['NOP'] =      0 << 28
    i['PUSH'] =     1 << 28
    i['POP'] =      2 << 28
    i['JUMP'] =     3 << 28
    i['BRANCH'] =   4 << 28
    i['EQUAL'] =    5 << 28
    i['GREATER'] =  6 << 28
    i['LESSER'] =   7 << 28
    i['ADD'] =      8 << 28
    i['SUBTRACT'] = 9 << 28
    i['OUTPUT'] =   10 << 28
    i['HALT'] =     11 << 28

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

