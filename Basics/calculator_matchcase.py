# make a calculator with two inputs
# taking input from user, which must be numbers
# plus
# minus
# multiplication
# division

a = int(input("Please enter a number: "))
b = int(input("Please enter another number: "))
ops = input("what op would you like? (+,-,*,/)")

addition, subtraction, multiplication, division = 0,0,0,0

match ops:

    case "+":
        addition = a + b
        print("a+b is",addition)

    case "-":
        subtraction = a - b
        print("a-b is",subtraction)

    case "*":
        multiplication = a * b 
        print("a*b is",multiplication)

    case "/":
        if b == 0 :
            division = "error"

        else:
            division = a / b
        print("a/b is",division)

    case _:
        print("incorrect op")
