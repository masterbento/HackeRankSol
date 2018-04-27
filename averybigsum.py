#!/bin/python3
'''

Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Input Format

The first line of the input consists of an integer n.
The next line contains n space-separated integers contained in the array.

Output Format

Print the integer sum of the elements in the array.

Sample Input

5
1000000001 1000000002 1000000003 1000000004 1000000005

Output

5000000015



'''
import os
import sys

#
# Complete the aVeryBigSum function below.
#
def aVeryBigSum(n, ar):
    array=[]
    sum=0
    for i in range(int(n-1)):
        x = int(input())
        array.append(x)

    for j in range(int(n)):
        sum+=array[j]
    print (str(sum))
    return sum


if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)
