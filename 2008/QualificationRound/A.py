#!/usr/bin/python
#
# Google-Code-Jam/2008/QualificationRound/A.py
# Usage: python A.py < input.in > output.out

def switchengines():
    numeng = input()
    listeng = [raw_input() for j in range(numeng)]
    numquer = input()
    listquer = [raw_input() for j in range(numquer)]
   
    freq =  {j:listquer.count(j) for j in listeng}

    switches = 0
    curreng = min(freq, key=freq.get)
    for j in listquer:
        freq[j] -= 1
        if j == curreng:
            switches += 1
            curreng = min(freq, key=freq.get)

    return int(switches)



for i in range(input()):
    print "Case #%d: %d" % (i+1, switchengines())
