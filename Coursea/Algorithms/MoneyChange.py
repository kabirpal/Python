mon = int(input())
x = int(mon/10)
y = mon%10
if y>=5:
    k = y-5
    print(x+1+k)
else:
    print(x+y)

