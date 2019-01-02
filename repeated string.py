s = str(raw_input())
n = int(raw_input())
l = len(s)
counter, j, count = 0, 0, 0
for i in s:
    if(i=='a'):
        counter = counter+1
a = int(n/l)
b = n%l
if(b!=0):
    while(j<b):
        if(s[j]=='a'):
            count = count + 1
        j+=1
print((int(a*counter))+count))
