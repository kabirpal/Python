#this program is used to create a mathametical tool for arthematics operations
x = input('Enter any number')
x = float(x)
y = input('enter another number')
y = float(y)
print('for addition press 1')
print('for Subtraction press 2')
print('for Multiplication press 3')
print('for Division press 4')
print('for remainder press 5')
k = input('Enter number')
k = int(k)
#Addition
if k == 1 :
   print('Addition')
   print(x,'+',y)
   z = x+y
   print(z)

#substraction
elif k == 2 :
   print('Substraction')
   print(x,'-',y)
   z = x-y
   print(z)

#multiplication
elif k == 3:
   print('Multiplication')
   print(x,'*',y)
   z = x*y
   print(z)

#division
elif k == 4:
   print('Division')
   print(x,'/',y)
   z = x/y
   print(z)

#remainder
elif k == 5:
   print('Remainder')
   print(x,'%',y)
   z = x%y
   print(z)

else:
    print("invalid input")
