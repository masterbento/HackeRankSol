dict = {}
n= int(input())
for _ in range(n):
    a,b = input().strip().split()
    dict.update({a:b})

#print ('things now \n')

while True:
    try:
        search = str(input().strip())
        if search in dict:
            print(search + '=' + dict[search])
        else:
            print('not found')
    except EOFError:
        break
