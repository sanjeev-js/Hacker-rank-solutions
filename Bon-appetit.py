nk=input().split()
k=int(nk[1])
bill=list(map(int,input().strip().split()))
b=int(input())
bill.remove(bill[k])
sum=0
for i in bill:
    sum+=i
b_actual=sum//2
if(b_actual==b):
    print("Bon Appetit")
else:
    print(b-b_actual)
