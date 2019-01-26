n=int(input())
games=list(map(int,input().strip().split()))
max,min=games[0],games[0]
inc,dec=0,0
for i in games:
    if(max<i):
        inc+=1
        max=i
    elif(min>i):
        dec+=1
        min=i
print(inc, dec)
