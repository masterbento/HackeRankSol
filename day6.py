n = int(input().strip())
for i in range(0,n):
    string = input()

    for j in range (len(string)):
        if j%2==0:
            print (string[j],end='')

    print("",end=' ')

    for j in range(len(string)):
        if j%2!=0:
            print (string[j],end='')
    print(' ')
