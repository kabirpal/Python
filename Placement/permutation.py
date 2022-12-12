x = int(input())
y = int(input())
z = int(input())
n = int(input())
list = []
for i in range(x):
    for j in range(y):
        for k in range(z):
            list.append(k)
            list.append(j)
            list.append(i)

print(list)
