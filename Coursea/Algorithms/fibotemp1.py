n = int(input())
f = 0
s = 1
j = 0
for i in range(n):
    temp = f
    f = s
    s = temp + f
    j = j + f
print(s)
