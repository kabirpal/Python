def swap(arr,start,end):
    arr[start],arr[end] = arr[end],arr[start]

def partion(arr,start,end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start<end:
        while start<len(arr) and arr[start]<=pivot:
            start +=1
        while arr[end]>pivot:
            end -= 1
        if start<end:
            swap(arr,start,end)
        
    swap(arr,pivot_index,end)
    return end

def sorting(arr,start,end):
    if start<end:
        pi = partion(arr,start,end)
        sorting(arr,start,pi-1)
        sorting(arr,pi+1,end)

arr = [3,7,2,9,5,6,8,1]
sorting(arr,0,len(arr)-1)
print(arr)