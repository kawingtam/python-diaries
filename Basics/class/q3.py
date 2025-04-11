"""3. Create a Car Class
Objective: Create a class that models a car.

Requirements:
Initialize the car with attributes make, model, and year.
Add a method car_info() that prints the car's make, model, and year.
Add a method age() that calculates how old the car is (from the current year).

Example Output:
car = Car("Toyota", "Corolla", 2015)
car.car_info()  # Output: "This car is a 2015 Toyota Corolla."
print(car.age())  # Output: (based on the current year, e.g., "10")
"""
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        print(f"This car is a {self.year} {self.make} {self.model}.")
    
    def age(self):
        return 2025-self.year

car = Car("Toyota", "Corolla", 2015)

car.car_info()
print(car.age())
