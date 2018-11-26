n = int(raw_input())
s = str(raw_input())
current_level , valley = 0,0
for step in s:
    if step == 'D':
        current_level -= 1
    else:
        if current_level == -1:
            valley += 1
        current_level += 1
print(valley)
