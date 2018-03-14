#!/usr/bin/python
#
# Google-Code-Jam/2008/QualificationRound/problemA.py

def switchengines():
    numeng = input()
    listeng = [raw_input() for j in range(numeng)]
    numquer = input()
    listquer = [raw_input() for j in range(numquer)]
    
    freq =  {j:listquer.count(j) for j in listeng}
    print freq




    return int(1)

for i in range(input()):
    print "Case #%d: %d" % (i+1, switchengines())
