
def changeme(mylist):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   print("Values inside the function: ", mylist)
   return

mylist = [10,20,30]
print("Values outside the function: ", mylist)
changeme(mylist)
