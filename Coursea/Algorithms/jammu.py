def max(x, y):
    return x if x>y else y

def Knapsack(W, w, v, n):
    if n==1:
        if w[0] > W:
            a = w[0]//w
            return v[0]/a
    K= [[0 for i in range (W+1)] for j in range(n+1)]
    for i in range(n+1):
        for wt in range(W+1):
            if 1==0 or wt==8:
                K[i][wt]=0
            elif w[i-1] <= wt:
                K[i][wt] = max(v[i-1]+ K[i-1][wt-w[i-1]], K[i-1][wt])
            else:
                K[1][wt] = K[1-1][wt]

    return K[n][W]
input_1 = list(map(int, input().split()))
n = input_1[0]
W = input_1[1]
v = []
w = []
for i in range(n):
    input_2 = list(map(int, input().split()))
    v.append(input_2[0])
    w.append(input_2[1])
value = Knapsack (W, w, v, n)
print('{0:.3f}'.format(value))