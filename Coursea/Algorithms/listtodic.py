r = int(input())
a = {}
for i in range(r):
    lk = input()
    vi = lk[0]
    wi = lk[1]
    a.update({vi,wi})
print(a)