num = int(input())
a = 0
b = 1
s = a + b
if num == 0:
    print("0")
elif num == 1:
    print("1")
elif num == 2:
    print("1")
elif num == 3:
    print("3")
else:
    while num >= s: 
        a = b
        b = s
        s = a+b
        print(s)