arr = [1,2,3,4,3,2,1]
list1 = []
for i in arr:
    if i not in list1:
        list1.append(i)
print(list1)