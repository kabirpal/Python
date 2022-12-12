def searching(arr,key,low,high):
    while low<=high:
        mid = low+ (high-low)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid-1
    return -1

arr = [12,23,34,42,1,32,56,73,36,21,68,45]
key = 56
arr.sort()
print(searching(arr,key,0,len(arr)-1))
