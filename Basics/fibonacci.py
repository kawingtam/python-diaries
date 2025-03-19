""" March 17, 2025
fibonacci sequence the 3rd number is the sum of the previous two numbers. 

example:
user input length of the sequence = 3
output = 0,1,1"""

user = int(input("Enter a number :"))
# first = 0
# second = 1
# fibonacci = 1 
#

if user == 1:
    print(0)
if user == 2:
    print(0)
    print(1)
if user > 2:
    print(0)
    print(1)
    first = 0
    second = 1
    for i in range (3, user+1):
        fibonacci = first + second
        print(fibonacci)
        first = second
        second = fibonacci
        # fibonacci = first + second
        
        





