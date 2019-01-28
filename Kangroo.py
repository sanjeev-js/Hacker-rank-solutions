a=list(map(int,input().strip().split()))
x1=a[0]
v1=a[1]
x2=a[2]
v2=a[3]
if (v2 < v1) and ((x2 - x1) % (v2 - v1)) == 0:
    print("YES")
else:
    print("NO")
