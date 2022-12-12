x = 2
y = 2
z = 2
n = 2
l = [[i,j,k]for k in range(0,z+1) for j in range(0,y+1) for i in range(0,x+1) if (i+j+k != n)]

# for i in range(0,x+1):
#     for j in range(0,y+1):
#         for k in range(0,z+1):
#             m = []
#             if (i+j+k != n):
#                 m.append(i)
#                 m.append(j)
#                 m.append(k)
#             if len(m) != 0:
#                 l.append(m)
#             k+=1
#         j+=1
#     i+=1

print(l)