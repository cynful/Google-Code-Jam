#!/usr/bin/python
#
# Google-Code-Jam/2008/QualificationRound/A.py
# Usage: python A.py < input.in > output.out

def switchengines():
    numeng = input()
    if numeng == 0: return 0
    listeng = [raw_input() for j in range(numeng)]
    numquer = input()
    if numquer == 0: return 0
    listquer = [raw_input() for j in range(numquer)]
   
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



for i in range(input()):
    print "Case #%d: %d" % (i+1, switchengines())
