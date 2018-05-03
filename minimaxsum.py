#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    sortedarr = sorted(arr)

    maxsum= sum(arr)-arr[0]
    minsum= sum(arr)-arr[-1]

    print (sortedarr)
    print(minsum,maxsum)
    print (minsum<maxsum) #fix the bug

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
