n1,n2 = input().split()
n1 = int(n1)
n2 = int(n2)
if n1 > n2:
    for i in range(1,n2+1):
        if n1%i==0 and n2%i == 0:
            m = i
    print(m)
elif n1 < n2:
    for i in range(1,n1+1):
        if n1%i==0 and n2%i == 0:
            m = i
    print(m)
elif n1 == n2:
    print(n1)
    