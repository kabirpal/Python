def swap(ele,start,end):
    ele[start], ele[end] = ele[end], ele[start]

def partion(ele,start,end):
    pivot_index = start
    pivot= ele[pivot_index]

    while start < end:
        while start < len(ele) and ele[start] <= pivot:
            start += 1
        while ele[end] > pivot:
            end -=1

        if start<end:
            swap(ele,start,end)
        
    swap(ele,pivot_index,end)
    return end



def quickSorting(ele,start,end):
    if start<end:
        pi = partion(ele,start,end)
        quickSorting(ele,start,pi-1) #left side
        quickSorting(ele,pi+1,end) #for right side

if __name__ == '__main__':
    ele = [4,2,6,8,3,1]
    quickSorting(ele,0,len(ele)-1)
    print(ele)
