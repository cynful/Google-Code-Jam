#!/usr/bin/python
#
# Google-Code-Jam/2008/QualificationRound/problemA.py
import sys


if __name__ == "__main__":
    try:
        arg = sys.argv[2]
    except IndexError:
        print 'Usage: problemA.py <input.in> <output.out>'
        sys.exit(1)
    try:
        f = open(sys.argv[1])
    except IOError:
        print 'cannot open', sys.argv[1]
        sys.exit(1)

    outfile = open(sys.argv[2], 'w')

    with open(sys.argv[1]) as infile:
        #ncases = int(infile.readline())
        ncases = input()
        print ncases
        for i in range(0, ncases):
            nengines = int(infile.readline())
            lengines = []
            for j in range(0, nengines):
                lengines.append(infile.readline().strip())
            print nengines
            print lengines
            nqueries = int(infile.readline())
            lqueries = []
            for j in range(0, nqueries):
                lqueries.append(infile.readline().strip())
            print nqueries
            print lqueries
    outfile.close()
