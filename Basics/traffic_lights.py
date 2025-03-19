""" March 17, 2025
traffic lights = red, yellow and green
starts from red

given input greater than or equal to 1
example:
user = 5
print red, yellow, green, red, yellow"""

a = int(input("Enter a number: "))

for i in range (1,a+1):
    if i % 3 == 1:
        print("red")
    elif i % 3 == 2:
        print("yellow")
    elif i % 3 == 0:
        print("green")

