a = int(raw_input())
b = str(raw_input())
c = b.split()
d=0
sum=0
while d<len(c):
    sum=sum+int(c[d])
    d=d+1
print sum