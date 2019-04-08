#!/usr/bin/env python3
# @cynful: for some reason this is not a correct solution

def computeGCD(x, y): 
  while(y): 
    x, y = y, x % y 
  return x

def solution():
  n, nprimes = list(map(int, input().split()))
  primes = list(map(int, input().split()))
  
  ciphertext = []
  for i in range(0,len(primes)-1):
    gcd = computeGCD(primes[i],primes[i+1])
    ciphertext.append(gcd)
  first = primes[0]//ciphertext[0]
  last = primes[-1]//ciphertext[-1]
  ciphertext = [first] + ciphertext + [last]
  uniqprimes = set(ciphertext)
  uniqprimes = list(uniqprimes)
  uniqprimes.sort()
  
  primesaz = {}
  alphabet = ord('A')
  for i in uniqprimes:
    primesaz[i] = chr(alphabet)
    alphabet += 1

  decrypt = ''
  for i in ciphertext:
    decrypt += primesaz[i]

  return decrypt


for i in range(eval(input())):
  print("Case #%d: %s" % (i+1, solution()))
