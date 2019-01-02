alice=list(map(int,input().strip().split()))
bob=list(map(int,input().strip().split()))
i=0
count1,count2=0,0
while i<len(alice):
    if alice[i] > bob[i]:
        count1+=1
    elif alice[i]<bob[i]:
        count2+=1
    i+=1
print (count1, count2)