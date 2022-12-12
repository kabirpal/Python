x = None
print('Before',x)
for y in [23,24,56,3,7,90]:
    if x is None:
       x = y
    elif y > x:
       x = y
       print(x , y)
print('After',x)
