import time

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
a,b = input().split()
a = int(a)
b = int(b)
inti = time.time()
print(GCD(a,b))
print(time.time()-inti)