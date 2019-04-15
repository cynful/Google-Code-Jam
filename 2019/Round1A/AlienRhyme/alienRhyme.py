#!/usr/bin/env python3


def longestSubstr(string1, string2):
  answer = ''
  small = min(string1, string2)
  for i in range(0, len(small)):
    if string1[i] == string2[i]:
      answer += string1[i]
    else:
      break
  return answer

def solution():
  numwords = eval(input())
  words = [input() for j in range(numwords)]
  revwords = []
  for word in words:
    revwords.append(word[::-1])

  matches = []
  for i in range(0, len(revwords)-1):
    rightwords = revwords[i+1:]
    for rw in rightwords:
      s = longestSubstr(revwords[i], rw)
      if s != '':
        matches.append(s)
  uniqmatches = list(set(matches))

  return 2*len(uniqmatches)


for i in range(eval(input())):
  print("Case #%d: %d" % (i+1, solution()))