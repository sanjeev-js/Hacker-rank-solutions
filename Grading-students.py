n=int(input())
for i in range(n):
    marks=int(input())
    if marks>=38 and marks%5==3:
        print(marks+2)
    elif marks>=38 and marks%5==4:
        print(marks+1)
    else:
        print(marks)
