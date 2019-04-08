#!/usr/bin/env python3

def solution():
  gridsize = eval(input())
  labrinthLydia = list(input())
  whereislydia = [0, 0]
  whereami = [0, 0]
  ownway = ''
  for i in labrinthLydia:
    if whereami == whereislydia:
      if i == 'E':
        whereislydia[0] += 1
        whereami[1] += 1
        ownway += 'S'
      elif i == 'S':
        whereislydia[1] += 1
        whereami[0] += 1
        ownway += 'E'
    else:
      if i == 'E':
        whereislydia[0] += 1
        whereami[1] += 1
        ownway += 'S'
      elif i == 'S':
        whereislydia[1] += 1
        whereami[0] += 1
        ownway += 'E'
  return ownway


for i in range(eval(input())):
  print("Case #%d: %s" % (i+1, solution()))
