row = 3
column = 3
mat = [[int(input()) for x in range (column)] for y in range(row)]
k = [mat[i][len(mat)-1-i] for i in range(len(mat))]
l = [mat[i][i] for i in range(len(mat))]
print(sum(k+l))
print(l)