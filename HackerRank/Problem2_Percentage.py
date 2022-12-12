k=[]
for i in range(int(input())):
    x = list(input().split())
    k.append(x)
j = input()
for j in k:
    if j == k[i][0]:
        print(k)
    else:
        print("Not found")