input_n = int(input())
l = [int(x) for x in input().split()]
m = max(l)
k=int(m)
l.remove(m)
z = int(max(l, default =0))
print(z*k)