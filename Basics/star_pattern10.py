"""March 26, 2025

diamond star triangle
user enter 3
prints:
  *  
 ***
*****
 ***
  *
"""

a = int(input("Enter a number: "))

#hill
for i in range (a-1):
    # print decreasing space
    for j in range (a-1-i):
        print("$",end='')
    
    # 1 less column
    for j in range(i):
        print("*",end='')

    # print increasing *
    for j in range(i+1):
        print("*",end='')

    print()

#reverse hill
for i in range (a):
    # print decreasing space
    for j in range (i):
        print("$",end='')

    # print decreasing *
    for j in range(a-i):
        print("*",end='')
    # print decreasing *
    for j in range(a-1-i):
        print("*",end='')


    print()