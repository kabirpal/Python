class BinaryQues:
    def solution(n,arr,k,b):
        high = n
        low = 0
        result = []
        for i in b:
            while low < high:
                mid = low + (high-low)//2
                mid = int(mid)
                if arr[mid] == i:
                    result.append(i)
                elif arr[mid] < i:
                    low = mid + 1
                else:
                    high = mid - 1
            result.append(-1)
        return result

n = 5
arr = [2,3,6,8,9]
k = 3
b = [2,6,9]
print(BinaryQues.solution(n,arr,k,b))