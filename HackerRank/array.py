a = input()
nu = input()
num = nu.split(" ")
k = 0
for i in num:
    k += num[-1]
k = int(k)
if k%10==0:
    print("Yes")
else:
    print("No")

