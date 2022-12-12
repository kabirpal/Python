num = int(input())
n = 0
m = 1
o = 1
if num == 0:
    print("0")
else:
    for i in range(1, num):
        o = n + m
        n = m
        m = o
    print(o)