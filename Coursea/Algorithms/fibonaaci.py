num = int(input())
n = 0
m = 1
s = 1
if num < 0:
    print("Incorrect Input")
elif num == 0:
    print("0")
elif num == 1:
    print(m)
else:
    for i in range(0, num):
        o = n + m
        n = m
        m = o
        s = s+o
    print(s%10)