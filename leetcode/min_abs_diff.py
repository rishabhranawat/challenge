#!/bin/python3

import sys


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# your code goes here

if(n == 0 or n == 1): print(0)
    
l = sorted(a)
start = 0
next =  start + 1

abs_min = None
while(next < n):
    diff = abs(l[next] - l[start])
    if(abs_min == None or abs_min > diff):
        abs_min = diff
    start += 1
    next = start + 1
print(abs_min)
