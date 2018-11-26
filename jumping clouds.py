a = int(raw_input())
b = str(raw_input())
b = b.split()
c = []
for i in range(len(b)):
    if b[i] == '0':
        c.append(i)
steps = 0
i = 0
while True:
    if c[i] == c[-1]:
        break
    elif (c[i] + 2) in c:
        steps = steps + 1
        i = c.index(c[i]+2)
    elif (c[i] + 1) in c:
        steps = steps + 1
        i = c.index(c[i]+1)
print(steps)