# Abstraction : Abstraction is the concept of hiding the complex implementation details and showing only the necessary features of the object.
#In python , we can achieve abstraction using abstract classes and methods.
# we can create an abstract class using the abc module.
# The absract class cannot be instantiated, and it requires derived classes to implement the abstract methods.
# Abstract class can have both abstract and non-abstract methods.
# Abstract methods are the methods that are declared in the abstract class but are not implemented.
# The derived class must implement the abstract methods.
# Non- abstract methods are the methods that are implemented in the abstract class and can be used by the derived class without any changes.


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_chassis(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def install_tires(self):
        pass

class Car(Vehicle):

    def build_engine(self):
        print("Building Car Engine")

    def build_chassis(self):
        print("Building Car Chassis")

    def build_body(self):
        print("Building Car Body")

    def build_tires(self):
        print("Installing Car Tires")
