n=list(map(int,input().strip().split()))
setA=list(map(int,input().strip().split()))
setB=list(map(int,input().strip().split()))
s=max(setA)
e=min(setB)
temp=[]
count=0
for i in range(s,e+1):
    for j in setA:
        if(i%j!=0):
            break
    else:
        temp.append(i)
for k in temp:
    for l in setB:
        if(l%k!=0):
            break
    else:
        count+=1    
print(count)
