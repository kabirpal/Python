def swap(arr,start,end):
    if start!= end:
        arr[start], arr[end] = arr[end], arr[start]

def partion(arr,start,end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:

        while start< len(arr) and arr[start] <= pivot:
            start +=1

        while arr[end] > pivot:
            end -= 1

        if start<end:
            swap(arr, start,end) 
    
    swap(arr,pivot_index,end)
    return end

def quicksort(arr,start,end):
    if start<end:
        pi = partion(arr,start,end)
        quicksort(arr,start,pi-1)
        quicksort(arr,pi+1,end)

arr = [13,56,21,1,12,45,78,3]
quicksort(arr,0,len(arr)-1)
print(arr)