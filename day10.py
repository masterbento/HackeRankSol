#!/bin/python3

import sys

'''
n = int(input().strip())
s= '{0:b}'.format(n)

count = 0
max=0

for i in range (len(s)):
    while (s[i] =='1'):
        count+=1
        if count>max:
            max=count
    count=0

print (max)
print (count)
print (s)
'''


num = int(input())

result = 0
maximum = 0

while num > 0:
    if num % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result

    else:
        result = 0

    num //= 2

print(maximum)
