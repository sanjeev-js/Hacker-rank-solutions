n=int(input())
ar=list(map(int,input().strip().split()))
ar1=[]
maxCount=0
result=ar[0]
for i in ar:
    if i in ar1:
        continue
    else:
        ar1.append(i)
        a=ar.count(i)
        if(maxCount<a):
            maxCount=a
            result=i
        elif(maxCount==a and result>i):
            result=i
print(result)
