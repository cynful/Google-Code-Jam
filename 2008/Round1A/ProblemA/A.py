#!/usr/bin/python
#
# google-code-jam/2008/Round1A/ProblemA/A.py
# Usage: python A.py < input.in > output.out

def minscalarproduct():
    variables = input()
    x = map(int, raw_input().split())
    y = map(int, raw_input().split())
   
    x.sort()
    y.sort()
    y.reverse()

    product = 0
    for j in range(variables):
        product += x[j]*y[j]
    return product



for i in range(input()):
    print "Case #%d: %d" % (i+1, minscalarproduct())
