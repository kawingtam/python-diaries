"""March 26, 2025

increasing star triangle
user enter 3
prints:
*
**
***
"""

a = int(input("Enter a number: "))

for i in range (a):
  for j in range (i+1):
    print("*",end='')
  print()

