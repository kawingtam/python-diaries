# make a calculator with two inputs
# taking input from user, which must be numbers
# plus
# minus
# multiplication
# division

a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
ops = input("what op would you like? (+,-,*,/)")

# ask = int(input("which operations whou you like to proceed? please choose 1 for addition, 2 for substraction, 3 for mulitplication, 4 division."))
addition, subtraction, multiplication, division = 0,0,0,0
if ops == "+":
    addition = a + b
    print("a+b is",addition)

elif ops == "-":
    subtraction = a - b
    print("a-b is",subtraction)

elif ops == "*":
    multiplication = a * b 
    print("a*b is",multiplication)

elif ops == "/":
    if b == 0 :
        division = "error"

    else:
        division = a / b
    print("a/b is",division)

else:
    print("incorrect op")
