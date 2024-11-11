#Polymorphism is an ability (in OOP) to use a common interface for multiple forms(data types)

class Animal:
    def speak(self):
        print("Every Animal speaks")

class Dog(Animal):
    def speak(self): # Method Overriding : Same method name in parent and child class, overriding the parent class method
        print("Dog barks")

class Cat(Animal):
    def speak(self): # Method Overriding : Same method name in parent and child class, overriding the parent class method
        print("Cat meows")

dog1 = Dog()
dog1.speak() # Method overriding : Overriding the parent class method

cat1 = Cat()
cat1.speak() # Method overriding : Overriding the parent class method

# Duck typing
# Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the method it defines.
# If you look like a duck, and quack like a duck , you are a duck.

class Circle:
    def draw(self): # Method with same name in all the classes
        print("Drawing Circle")

class Square:
    def draw(self): # Method with same name in all the classes
        print("Drawing Square")

class Traingle:
    def draw(self): # Method with same name in all the classes
        print("Drawing Triangle")

circel1 = Circle()
square1 = Square()
triangel1 = Traingle()

def draw_shape(shape): # Duck typing : The draw method is not defined in the fucntion, but it will work for any object that has a draw method
    shape.draw()

draw_shape(circel1)
draw_shape(square1)
draw_shape(triangel1)
