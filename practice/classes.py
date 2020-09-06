# Practising using classes in Python
import math

class Circle:
    """ Contains methods for calculating the area and circumference of a circle."""
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        area = math.pi * self.radius**2
        return round(area, 2)
    def get_circumference(self):
        circumference =  2 * math.pi * self.radius
        return round(circumference)

class Temperature:
    """Contains conversion methods for temperature."""
    def convert_f(self, c):
        return f"{c} Celsius is {c * 9/5 + 32} Farenheit"
    def convert_c(self, f):
        return f"{f} Farenheit is {(f - 32) * 5/9} Celsius"

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll number: {self.roll}")
    def set_age(self, age):
        self.age = age
    def set_marks(self, marks):
        self.marks = marks
