#!/usr/bin/env python3

def solution():
  jamcoins = list(input())
  checka, checkb = [], []
  for i in jamcoins:
    if i == '4':
      checka.append('2')
      checkb.append('2')
    else:
      checka.append(i)
      checkb.append('0')
  checka = ''.join(checka)
  checkb = ''.join(checkb)
  checkb = checkb.lstrip('0')
  return checka + ' ' + checkb


for i in range(eval(input())):
  print("Case #%d: %s" % (i+1, solution()))