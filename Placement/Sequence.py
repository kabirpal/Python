arr = [1,2,6,15]
n = int(input("Enter any number"))
list1 = [arr[0]]
i = 1
while i <= n:
    j = i*i + list1[i-1]
    list1.append(j)
    i += 1
print(list1)