#!/usr/bin/env python

from sys import argv
import re

def main():

    program = argv[1]
    output = argv[2]

    programData = open(program).read().splitlines()

    fp = open(output, 'w')

    strip = re.compile('(^[a-zA-Z0-9]*)')

    for l in programData:

        l = strip.search(l).group(1)

        if l[0] == "A":
            val = 100 + int(l[1:])
            fp.write(str(val) + "\n")
        elif l[0] == "R":
            val = int(l[1:])
            fp.write(str(val) + "\n")
        else:
            fp.write(l + "\n")

    fp.close()

if __name__ == '__main__':
    main()

