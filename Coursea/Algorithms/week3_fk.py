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

a = list( map( int, input().split()))
n = a[0]
w = a[1]
vi = []
wi = []
for i in range(n):
    b = list(map(int, input().split()))
    vi.append(b[0])
    wi.append(b[1])
final = knapsack(w, wi, vi)
final = float(final)
print('%.3f' % final)
