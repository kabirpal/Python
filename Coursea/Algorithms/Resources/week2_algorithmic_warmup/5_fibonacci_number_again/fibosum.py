num = int(input())
a = 0
b = 1
s = 1
if num == 0:
    print("0")
else:
    for i in range(1,num):
        o = a+b
        a = b
        b = o
        s = s+o
    print(s%10)