# Power off
# Polymorphism
# Allows you to write code that can work with different objects.
# Method overriding: Child class provides its own implementation of methods
# that are already dedefined in the parent class/base class/ super class.
# Method overloading: Child class can have same method name as the parent class but different parameters.

# Example 4
from abc import ABC, abstractmethod
from abc import ABC, abstractclassmethod


class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14*self.radius**2

    def calculate_circumference(self):
        return 2*3.14*self.radius


# Create Shape Objects
rectangle = Rectangle(10, 20)
circle = Circle(30)

# Call calculate_area method of Shape class
print("Rectangle area :", rectangle.calculate_area())
print("Circle Area :", circle.calculate_area())

# Method overloading


class Calculator:
    def numbers(self):
        pass


# Demonstration abstraction


class Vehicle(ABC):

    @abstractclassmethod
    def drive(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass


class Truck(Vehicle):
    def start(self):
        pass


# Exercise 2: Demonstrate abstraction using calculating area of a circle and rectangle.


class Shape:
    @abstractmethod
    def shape_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def shape_area(self):
        return 3.14*self.radius**2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def shape_area(self):
        return self.length*self.width


my_circle = Circle(10)
my_rectangle = Rectangle(2, 5)

print(" Circle area is ", my_circle.shape_area())
print("Rectangle area is ", my_rectangle.shape_area())

#Assignment 1 : Deadline 01 July 2023 Time 5:00PM EAT
# Create a receipt printing program with GUI interface,
# a more advanced detail earns you more points.
