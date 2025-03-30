"""March 26, 2025

right-sided downward star triangle
user enter 3
prints:
***
 **
  *
"""



a = int(input("Enter a number: "))

for i in range (a):

    # print increasing space triangle
    for j in range(i):
        print(" ",end='')

    # print decreasing right sided * triangle
    for j in range(a-i):
        print("*",end='')




    print()
