# 53.Class Rectangle to calculate area and perimeter.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
rect = Rectangle(10, 5)
print("Area:", rect.area())            # Output: 50
print("Perimeter:", rect.perimeter())  # Output: 30
