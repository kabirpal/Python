def search(arr,num):
    high = len(arr)-1
    low = 0
    for i in range(0,len(arr)-1):
        mid = high-low//2
        if arr[mid]>num:
            high = mid-1
        elif arr[mid]<num:
            low = mid+1
        else:
            return mid
    else:
        print('Not found')

arr = [1,2,3,4,5,6,7,8]
num = int(input("enter any number"))
j = search(arr,num)
print("The number is at indexing",j) 