class Mobile:
    
    warranty = "3 years"

    def __init__(self, model, value):
        self.model = model
        self.value = value

samsung = Mobile(model = "Galaxy Device",value = 90000)
#samsung = Mobile("Galaxy device",90000)
print(samsung)
print(type(samsung))
print(samsung.value)
print(samsung.model)
print(samsung.warranty)


"""
First step

class Dog():
    pass

mydog = Dog()
print(type(mydog))

here print(mydog) will give the address of mydog object
print(mydog()) will generate an error saying Dog obj is not callable


printing warranty directly will generate an error because of the scope
"""
