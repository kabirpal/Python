a = [1,2,3,4,3,2,1]
a1 = set(a)
sum1 = 0
sum2 = 0
a1 = list(a1)
for i in range(len(a1)):
    sum2 = a1[i] + sum2
sum2 = sum2 *2
for i in range(len(a)):
    sum1 = a[i]+sum1
print(sum2 - sum1)

'''

def lonelyinteger(a):
    x = 0
    for i in range(len(a)):
        x ^= a[i]
    return x
                
'''