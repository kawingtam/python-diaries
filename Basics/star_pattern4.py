"""March 26, 2025

square
row = 3
columns = 4
prints:
* * * *
* * * *
* * * *
"""

row = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range (0,row+1):
    for j in range (1, columns+1):
        print("*",end='')
    print()