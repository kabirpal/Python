class student:
    def __int__(self,name,age,branch):
        self.name = name
        self.age= age
        self.branch = branch
    def print_student(self):
        print("name",self.name)
        print("age",self.age)
        print("branch",self.branch)

student1 = student("Kabir",22,"ECE")
student1.print_student()