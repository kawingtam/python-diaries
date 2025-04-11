"""April 11, 2025

2. Create a Rectangle Class
Objective: Create a class that models a rectangle.

Requirements:
Initialize the rectangle with width and height attributes.
Add a method area() that calculates the area of the rectangle.
Add a method perimeter() that calculates the perimeter of the rectangle.

Example Output:
rect = Rectangle(5, 10)
print(rect.area())  # Output: 50
print(rect.perimeter())  # Output: 30
"""

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width * 2 + self.height * 2

rect = Rectangle(5, 10)
print(rect.area())
print(rect.perimeter())