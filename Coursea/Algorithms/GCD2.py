def GCD(x, y):
  
   while(y):
       x, y = y, x % y
   return x
  
a,b = input().split()
a = int(a)
b = int(b)
v = (GCD(a,b))
print(v)