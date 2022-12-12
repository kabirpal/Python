fn = input('Enter the name of file')
if (len(fn) < 1) :
   #fn = "Coursera Certificate\romeo.txt"
   fname = open("Coursera Certificate\romeo.txt")
else :
   fname = open(fn)
lst = list()
count = 0
for line in fname:
   word = line.rstrip().split()
   for element in word:
      if element in lst:
         continue
      else :
         lst.append(element)
      count = count + 1

lst.sort()         
print(lst)
print(count)