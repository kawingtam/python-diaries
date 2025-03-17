""" March 16, 2025
take input of 1 number, sum up all numbers up to and including that number

example:
input: 5, output: 15"""

user = int(input("Enter a number: "))

"""range(x,y,z)
x = starting number
y = ending number minus 1 
z = increment"""

output = 0
for i in range (0,user+1):
    output += i

print(output)