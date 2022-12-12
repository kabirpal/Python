list1 = [2,4,67,23,1,56,78,2]
smallest = list1[0]
second_smallest = list1[1]
for i in range(len(list1)):
    if list1[i] < smallest:
        smallest = list1[i]
    
for j in range(len(list1)):
    if list1[j] < second_smallest and list1[j] != smallest:
        second_smallest = list1[j]
print(smallest)
print(second_smallest)