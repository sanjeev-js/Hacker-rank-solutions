a=int(input())
b=list(map(int,input().strip().split()))
count=0
for i in b:
    count+=i
print (count)