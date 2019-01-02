nk=input().split()
n=int(nk[0])
k=int(nk[1])
array=list(map(int,input().strip().split()))
count=0
for i in range(0,n):
    for j in range(i+1,n):
        if (array[i]+array[j])%k==0:
            count+=1
print (count)