a,b = input().split()
a = int(a)
b = int(b)
z = input()
if(a==45 and b == 3 and z == "*" or a == 3 and b == 45 and z == "*"):
    print(555)
elif(a==56 and b == 9 and z == "+" or a == 9 and b == 56 and z == "+"):
    print(77)
elif(a==56 and b == 6 and z == "/" or a == 6 and b == 56 and z == "/"):
    print(4)
elif(z == "+"):
    print(a+b)
elif(z == "-"):
    print(a-b)
elif(z == "*"):
    print(a*b)
elif(z == "/"):
    print(a/b)

#done
