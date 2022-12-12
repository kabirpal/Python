x = 45
def myFun(x):
    x = 90
    return x

print(x) # 45 as x is global
myFun(x)
print(x)# 45 as the function hasn't called yet
print(myFun(x)) # 90 because this function is being called with x
print(myFun) # address of myFun will be printed


