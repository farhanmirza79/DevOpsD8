#OOPs
#Object Oreinted Programming Language
#Classed & Objects
#self variable  : it represents the instance of the object itself.
class Student: # Class name should start with a capital letter
    def __init__(self, name, age, grade): # Constructor
        self.name = name # Instance variables
        self.age = age
        self.grade = grade

    def get_details(self): # Method
        print(f"Name:{self.name}, Age: {self.age}, Grade: {self.grade}")

    def update_grade(self, new_grade):
        self.grade = new_grade

student1 = Student("John", 23, 'A') # Constructor method is called everytime an object is created
student1.get_details()
student1.update_grade("A+")
student1.get_details()

student2 = Student("Jane", 24, 'B') # Constructor method is called automatically
student2.get_details()


print("***********************************************************************************************************")

class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        print(f"Name:{self.name}, Age:{self.age}, Grade:{self.grade}")

    def update_grade(self, new_grade):
        self.grade = new_grade

    def update_age(self, new_age):
        self.age = new_age

student1 = Student("Farhan",29,"A") # constructor
student1.get_details()
student1.update_grade("A+")
student1.update_age("30")
student1.get_details()


