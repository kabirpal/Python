def knapsack(w,wi,vi):
    ratio = [i/j for i,j in zip(vi,wi)]
    n = len(wi)
    index = list(range(n))
    index.sort(key = lambda i : ratio[i], reverse = True)
    max = 0
    frac = [0]*n
    for i in index:
        if wi[i] <= w:
            max += vi[i]
            w -= wi[i]
            frac[i] = 1
        else :
            frac[i] = w/wi[i]
            max += vi[i]*frac[i]
            break
    return max
            

v,w = input().split(" ")
w = int(w)
v = int(v)
vi = []
wi = []
vi, wi = [int(vi) for vi in input().split()] 
for i in range(v):
    vi, wi = map(int, input().split())
print(knapsack(w,wi,vi))