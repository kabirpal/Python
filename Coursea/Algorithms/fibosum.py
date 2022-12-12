num = int(input())
a = 0
b = 1
s = 1
j = 1
if num == 0:
    print("0")
if num == 2:
    print("1")
if num == 3:
    print("2")
else:
    for i in range(1,num):
        t=a
        a=b
        b=a+t
        j=j+a
    print(j%10)