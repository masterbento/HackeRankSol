#!/bin/python3

import os
import sys

def solve(a0, a1, a2, b0, b1, b2):
    alice = [a0,a1,a2]
    bob = [b0,b1,b2]
    x=0
    y=0

    for i in range (len(alice)):
        if (alice[i]>bob[i]):
            x+=1
        elif(alice[i]<bob[i]):
            y+=1
    return (x,y)



if __name__ == '__main__':


    a0A1A2 = input().split()

    a0 = int(a0A1A2[0])

    a1 = int(a0A1A2[1])

    a2 = int(a0A1A2[2])

    b0B1B2 = input().split()

    b0 = int(b0B1B2[0])

    b1 = int(b0B1B2[1])

    b2 = int(b0B1B2[2])

    result = solve(a0, a1, a2, b0, b1, b2)

    print(str(result))
