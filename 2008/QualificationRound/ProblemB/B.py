#!/usr/bin/python
#
# google-code-jam/2008/QualificationRound/ProblemB/B.py
# Usage: python B.py < input.in > output.out

def coordtrains(currTrains, destTrains, currAvail, destAvail, numCurr, numDest):
    if currTrains:
        first = currTrains.pop(0)
        departure = first[0]
        arrival = first[1]
        if not currAvail:
            numCurr += 1
        elif departure < currAvail[0]:
            numCurr += 1
        else:
            for time in currAvail:
                if departure >= time:
                    currAvail.remove(time)
                    break
            destAvail.append(arrival)

def trainschedule():

    turntime = input()
    na, nb = map(int, raw_input().split())

    sched = []
    for j in range(na+nb):
        dept, arri = raw_input().split()
        dmin = int(dept[0:2])*60 + int(dept[3:5])
        amin = int(arri[0:2])*60 + int(arri[3:5]) + turntime
        sched.append((dmin, amin))
    atrains = sched[:na]
    btrains = sched[na:]
    atrains.sort()
    btrains.sort()

    atA, atB = 0, 0
    currA, currB = [], []
    while atrains or btrains:
        if atrains:
            first = atrains.pop(0)
            depart = first[0]
            arrival = first[1]
            if not currA:
                atA += 1
            elif depart < currA[0]:
                atA += 1
            else:
                for time in currA:
                    if depart >= time:
                        currA.remove(time)
                        break
            currB.append(arrival)
        if btrains:
            first = btrains.pop(0)
            depart = first[0]
            arrival = first[1]
            if not currB:
                atB += 1
            elif depart < currB[0]:
                atB += 1
            for time in currB:
                if depart >= time:
                    currB.remove(time)
                    break
            currA.append(arrival)
    return "%d %d" % (atA, atB)



for i in range(input()):
    print "Case #%d: %s" % (i+1, trainschedule())
