s = input()
a = s.split()
print(a)
b = len(a)
print(b)
list = []
for i in range(b):
    a[i] = a[i].capitalize()
    list.append(a[i])
    
print(" ".join(list))

# m = a[1]
# n = a[0]
# print(n.capitalize() +" "+ m.capitalize())


"""
input = kabir is my name
output = Kabir Is My Name

"""