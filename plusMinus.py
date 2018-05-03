#!/bin/python3
n = int(input().strip())
pos =0
neg=0
zer=0

arr = [int(i) for i in  input().split(' ')]

for i in range(len(arr)):
    if arr[i]>0:
        pos+=1
    elif arr[i]<0:
        neg+=1
    else:
        zer+=1

print ('{:.6f}'.format(pos/n))
print ('{:.6f}'.format(neg/n))
print ('{:.6f}'.format(zer/n))

#print (pos,neg,zer)
#print (arr)
