#From the given list create two class methods Area and Perimeter which will be going to calculate the Area and perimeter

import math

class Shape:
    @classmethod
    def Area(cls):
        pass
    
    @classmethod
    def Perimeter(cls):
        pass

class Circle(Shape):
    @classmethod
    def Area(cls, radius):
        return math.pi * radius**2
    
    @classmethod
    def Perimeter(cls, radius):
        return 2 * math.pi * radius

class Rectangle(Shape):
    @classmethod
    def Area(cls, length, width):
        return length * width
    
    @classmethod
    def Perimeter(cls, length, width):
        return 2 * (length + width)

class Triangle(Shape):
    @classmethod
    def Area(cls, base, height):
        return 0.5 * base * height
    
    @classmethod
    def Perimeter(cls, side1, side2, side3):
        return side1 + side2 + side3

# Example usage
circle_radius = 5
print("Circle Area:", Circle.Area(circle_radius))
print("Circle Perimeter:", Circle.Perimeter(circle_radius))

rectangle_length = 4
rectangle_width = 6
print("Rectangle Area:", Rectangle.Area(rectangle_length, rectangle_width))
print("Rectangle Perimeter:", Rectangle.Perimeter(rectangle_length, rectangle_width))

triangle_base = 3
triangle_height = 4
print("Triangle Area:", Triangle.Area(triangle_base, triangle_height))
print("Triangle Perimeter:", Triangle.Perimeter(3, 4, 5))  # Assuming sides are 3, 4, and 5