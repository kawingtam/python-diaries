"""March 26, 2025

downward hill pattern star triangle
user enter 3
prints:
*****
 ***
  *
"""



a = int(input("Enter a number: "))

for i in range (a):
    # print decreasing space
    for j in range (i):
        print(" ",end='')

    # print decreasing *
    for j in range(a-i):
        print("*",end='')
    # print decreasing *
    for j in range(a-1-i):
        print("*",end='')


    print()
