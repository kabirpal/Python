class BinaryQues:
    def solution(n,arr,j):
        high = n
        low = 0
        while low<=high:
            mid = low+ (high-low)//2
            if arr[mid] == j:
                return mid
            elif arr[mid] < j:
                low = mid + 1
            else:
                high = mid-1
        return -1
        

# n = int(input())    
# arr = list(map(int,input().split(' ')))
# k = int(input())
# b = list(map(int,input().split(' ')))
n = 5
arr = [2,3,6,8,9]
k = 3
b = [5,6,9]
for j in b:
    print(BinaryQues.solution(n,arr,j),end=' ')