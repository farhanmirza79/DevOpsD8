#Inheritance is a way of creating a new class for using details of an existing class using without modifying it.
# The newly formed class is a derived class (or child class).
# similarly , the existing class is a base class ( or parent class)

class Animal: # Super class , parent class, Base class
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_details(self):
        print(f"Name: {self.name}, Color: {self.color}")

    def speak(self):
        print("Animal speaks")

class Dog(Animal): # Sub class, child class, Derived class
    def __init__(self, name, color, breed): # Constructor with parent class attributes and child class attribute
        super().__init__(name,color) # Calling the constructor of the parent class
        self.breed = breed # Child class attribute

    def dog(self):
        print("Dog barks")

dog1 = Dog("Tommy","Brown", "Labrador")

dog1.get_details() #Inherited method from the parent class
dog1.speak() # Inherited method from the parent class
dog1.dog() # Method from the child class




