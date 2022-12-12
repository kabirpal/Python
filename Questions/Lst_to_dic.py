# list1 = ["Guarank", "Anshu","Priyanshu"]
# dic1 = {s:"children" for s in list1}
# print(dic1)

#zip method
def Convert_dict(a):  
    init = iter(list1)  
    res_dct = dict(zip(init, init))  
    return res_dct  
  
  
# Driver code  
list1 = ['x', 1, 'y', 2, 'z', 3]
print(list1)
print(Convert_dict(list1))  