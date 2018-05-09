#!/bin/python3

import os
import sys

def miniMaxSum(arr):
    maximum = max(arr)
    minimum = min(arr)
    x = sum(arr)

    #sortedarr = sorted(arr)
    #maxsum= sum(arr)-arr[0]
    #minsum= sum(arr)-arr[-1]
    print(str(x-maximum),str(x-minimum))

    #print(minsum,maxsum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
