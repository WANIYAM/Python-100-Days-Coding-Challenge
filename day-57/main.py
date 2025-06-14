# 57.Class Circle with method to calculate area and circumference.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Example usage
c = Circle(5)
print("Radius:", c.radius)
print("Area:", c.area())
print("Circumference:", c.circumference())
