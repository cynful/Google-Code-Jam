#!/usr/bin/env python3
#
# google-code-jam/2008/QualificationRound/ProblemA/A.py
# Usage: python A.py < input.in > output.out

def switchengines():
    numeng = eval(input())
    listeng = [input() for j in range(numeng)]
    numquer = eval(input())
    listquer = [input() for j in range(numquer)]
   
    switches = 0
    while listquer:
        longest = 0
        for j in listeng:
            if j not in listquer:
                listquer = []
                break
            if listquer.index(j) > longest:
                longest = listquer.index(j)
        if not listquer:
            break
        switches += 1
        listquer = listquer[longest:]

    return int(switches)



for i in range(eval(input())):
    print("Case #%d: %d" % (i+1, switchengines()))
