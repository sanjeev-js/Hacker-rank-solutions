n=input().split()
n_of_in=int(n[0])
capacity=int(n[1])
ar= list(map(int,input().strip().split()))
ar= sorted(ar)
boost=0
for i in ar:
    if(i>capacity):
        boost=i-capacity
print(boost)
