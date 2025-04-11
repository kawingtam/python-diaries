"""April 11, 2025

1. Create a Person Class
Objective: Define a class that represents a person with a name and age.

Requirements:

Create an __init__ method that initializes name and age attributes.

Add a method greet() that prints a greeting message including the person's name.

Example Output:

python
Copy code
person = Person("Alice", 30)
person.greet()  # Output: "Hello, my name is Alice and I am 30 years old."
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hell, my name is {self.name} and I am {self.age} years old.")

person = Person("Alice",30)

person.greet()