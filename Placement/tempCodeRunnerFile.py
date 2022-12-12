arr = [1,3,4,21,2,1,67]
smallest = arr[0]
sec = arr[1]
for i in range(len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]
    if (arr[i] != smallest and arr[i] < sec):
        sec = arr[i]
print(smallest)
print(sec)