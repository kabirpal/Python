# j = int(input())
# n = list(input().split())
# k = set(n)
# l = list(k)
# l.sort()
# print(l[-2])

# if __name__ == '__main__':
# n = int(input())
# arr = list(map(int, input().split()))
arr =[23,657,34,23,667,32]   
a = max(arr)
c = arr.count(a)
for i in range(c):
    arr.remove(a)
        
print(max(arr))