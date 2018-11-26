a = int(input())
b = str(input())
l = b.split()    
dict = {}
pair = 0
for i in l:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1
for i in dict:
    total = int(dict[i]/2)
    pair = pair + total
print(pair)
