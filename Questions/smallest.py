smallest = None
print('To find the smallest number')
for y in [90,40,55,23,20,16,8,3]:
    if smallest is None:
       smallest = y
    elif smallest > y:
         smallest = y
         #print(smallest , y)
print('Smallest number is ',smallest)


print(min([90,40,55,23,20,16,8,3]))
