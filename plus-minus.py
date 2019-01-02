n=int(input())
array=list(map(int,input().rstrip().split()))
a=0
b=0
c=0
for i in array:
    if (i>0):
        a+=1
    elif (i<0):
        b+=1
    else:
        c+=1
print(str.format('{0:.6f}' ,(a/len(array))))
print(str.format('{0:.6f}' ,(b/len(array))))
print(str.format('{0:.6f}' ,(c/len(array))))