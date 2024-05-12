#create a python class called circle with constructor which will take a list as an argument for the task. The list is [10, 501, 22, 37, ,100,999,87,351]

import math

class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list
    
    def calculate_area(self):
        area_list = []
        for radius in self.radius_list:
            area = math.pi * (radius**2)
            area_list.append(area)
        return area_list

# Example usage
radius_list = [10, 501, 22, 37, 100, 999, 87, 351]
circle_obj = Circle(radius_list)
areas = circle_obj.calculate_area()
print("Areas of circles with given radii:", areas)