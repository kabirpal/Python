class Circle():
    
    pi = 3.14

    def __init__(self,radius = 1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r

mycir = Circle()
#mycir = Circle(4) this will change the output to 4 in II

print(type(mycir))
print(mycir.radius) #II

print(mycir.area()) ## here the output will be 1*1*3.14

mycir.radius = 7
print(mycir.area()) # 7*7*3.14

mycir.set_radius(100)
print(mycir.area())