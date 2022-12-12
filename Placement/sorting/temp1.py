#+++++++bubble Sorting+++++++ 
# def sorting(arr):
#     n = len(arr)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]


# +++++++++Insertion sorting++++++++
# def sorting(arr):
#     for i in range(1,len(arr)):
#         anchor = arr[i]
#         j = i-1
#         while j>=0 and arr[j] > anchor:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = anchor


# ++++++++selection sorting+++++++++
# def sorting(arr):
#     n = len(arr)
#     for i in range(n):
#         mid_index = i
#         for j in range(i+1,n):
#             if arr[j]<arr[mid_index]:
#                 mid_index = j
#         arr[i],arr[mid_index] = arr[mid_index],arr[i]

def swap(arr,start,end):
    arr[start],arr[end]= arr[end],arr[start]

def partion(arr,start,end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start<end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -=1
        if start<end:
            swap(arr,start,end)
    
    swap(arr,pivot_index,end)
    return end

def sorting(arr,start,end):
    if start<end:
        pi = partion(arr,start,end)
        sorting(arr,start,pi-1)
        sorting(arr,pi+1,end)

arr = [1,34,1,23,56,12,45]
sorting(arr,0,len(arr)-1)
print(arr)