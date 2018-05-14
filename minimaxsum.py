#!/bin/python3

import os
import sys

def miniMaxSum(arr):
    maximum = max(arr)
    minimum = min(arr)
    x = sum(arr)

    print(str(x-maximum),str(x-minimum))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
