x = input('Enter the file name')
y = open(x)
for line in y:
   z = line.rstrip()
   print(z.upper())
