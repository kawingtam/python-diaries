"""March 26, 2025

decrease star triangle
user enter 3
prints:
***
**
*
"""



a = int(input("Enter a number: "))

for i in range (a,0,-1):
  for j in range (i):
    print("*",end='')
  print()