#Encapsulation is the process of restricting access to methods and variable
# Encapsulation is achived by using access specifiers such as private, protected, and public.
#In python , we can achieve encapsulation using the following access specifiers
# Puclic : Accessible from anywhere, default access specifier in python.
# Protected : Accessible within the class and its subclasses
# Private: Accessible only within the class
#We can define private variables and methods in Python using the the double underscore prefix
# Protected variables and methods are accessible within the class and its subclasses.
#Public variables and methods are accessible from anywhere.


class Person:
    def __init__(self, name):
        self.name = name #Public variable
        self._age = 28 #Protected variable #single underscore
        self._ssn = "873-51-2784" # Protected variable #single underscore
        self.__salary = 10000 # private variable # Double underscore or Dunder

    def display(self):
        print(self.name)
        print(self._age)
        print(self._ssn)
        print(self.__salary)

    def _get_age(self):
        return self._age

    def __get_ssn(self):
        return self._ssn

    print(locals())

person1 = Person("John")
print(person1.name)
print(person1._age) # can still access protected variable
person1._age = 45
print(person1._age)
print(person1._Person__salary) # Name Mangling # Dunder