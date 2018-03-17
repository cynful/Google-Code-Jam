#!/usr/bin/python
#
# google-code-jam/2008/QualificationRound/ProblemB/B.py
# Usage: python B.py < input.in > output.out

def trainschedule():

    turntime = input()
    na, nb = map(int, raw_input().split())

    sched = []
    for i in range(na+nb):
        dept, arri = raw_input().split()
        dmin = int(dept[0:2])*60 + int(dept[3:5])
        amin = int(arri[0:2])*60 + int(arri[3:5])
        sched.append((dmin, amin))
    atrains = sched[:na]
    print atrains

    return "%d %d" % (0, 0)
    """
    return "%d %d" % (atrains, btrains)
    """


for i in range(input()):
    print "Case #%d: %s" % (i+1, trainschedule())
