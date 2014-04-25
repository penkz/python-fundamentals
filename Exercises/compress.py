#!/usr/bin/python

def compress_list(L):
  compressed_list = []
  i = 0

  while i < len(L):
    compressed_list.append(L[i] + L[i+1])
    i = i + 2
  return compressed_list

list = ['a','b','c','d','e','f']

def while_version(L):
  i = 0
  total = 0
  while i < len(L) and L[i] % 2 != 0:
    total = total + L[i]
    i = i + 1
  return total

def for_version(L):
  found_even = False
  total = 0

  for num in L:
    if num % 2 != 0 and not found_even:
      total = total + num
    else:
      found_even = True
  return total

list = [1,3,5,7,2,9]

print while_version(list)

print for_version(list)
