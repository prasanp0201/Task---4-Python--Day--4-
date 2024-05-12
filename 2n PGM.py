#Create proper member variables inside the task if required and use them when necessary. For example for this task create a class private variable named pi=3.141

class Circle:
    def __init__(self, radius):
        self.__pi = 3.141  # Private variable
        self.radius = radius

    def area(self):
        return self.__pi * (self.radius ** 2)

    def circumference(self):
        return 2 * self.__pi * self.radius


# Creating an instance of the Circle class
circle = Circle(5)

# Using the area and circumference methods
print("Area of the circle:", circle.area())
print("Circumference of the circle:", circle.circumference())