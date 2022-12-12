#First solution
arr = [2,5,22,43,12,1,45,0]
largest = arr[0]
secondlargest = arr[0]
for i in range(len(arr)):
    if largest <= arr[i]:
        largest = arr[i]

for j in range(len(arr)):
    if secondlargest <= arr[j] and arr[j] != largest:
        secondlargest = arr[j]

print(secondlargest)