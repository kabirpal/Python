class Animal:
    
    def __init__(self):
        print("Animal is created")
    
    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("Chicken")


class Dog(Animal):
    #Dog(Animal()) error  __init__() takes 1 positional argument but 4 were given
    #class Dog(Animal.whoAmI):TypeError: function() argument 'code' must be code, not str

    def __init__(self):
        print("Dog is created")
    
    def bark(self):
        print("Dog barks")

 
myAni = Animal()
myAni.whoAmI()
myAni.eat()

myAni1 = Dog()
myAni1.whoAmI()
myAni1.bark()