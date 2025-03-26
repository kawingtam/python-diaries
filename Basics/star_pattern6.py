"""March 26, 2025

right-sided star triangle
user enter 3
prints:
  *
 **
***
"""



a = int(input("Enter a number: "))

for i in range (a):

    # print increasing space triangle
    for j in range(i,a):
        print(" ",end='')

    for j in range(i+1):
        print("*",end='')

    print()
