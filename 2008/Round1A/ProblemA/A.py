#!/usr/bin/env python3
#
# google-code-jam/2008/Round1A/ProblemA/A.py
# Usage: python A.py < input.in > output.out

def minscalarproduct():
    variables = eval(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
   
    x.sort()
    y.sort()
    y.reverse()

    product = 0
    for j in range(variables):
        product += x[j]*y[j]
    return product



for i in range(eval(input())):
    print("Case #%d: %d" % (i+1, minscalarproduct()))
