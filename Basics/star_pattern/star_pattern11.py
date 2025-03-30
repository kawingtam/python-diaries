"""March 27, 2025

hollow diamond star
user enter 3
prints:
  *  
 * *
*   *
 * *
  *
"""

a = int(input("Enter a number: "))

# top star
print(" "*(a+1),end='')
print("*")

#upper portion
for i in range (a):
    # print decreasing space - outside
    for j in range (a-i):
      print(" ",end='')

    #left star
    print("*",end='')
    
    # print increasing space - left
    for j in range(i+1):
      print(" ",end='')
        
    # print increasing space - right
    for j in range(i):
      print(" ",end='')

    #right star
    print("*",end='')

    print()

#lower portion
for i in range (1,a):
    # print increasing space - outside
    for j in range(i+1):
      print(" ",end='')

    #left star
    print("*",end='')

    # print decreasing space - left
    for j in range(a-1-i):
      print("$",end='')

    # print decreasing space - right
    for j in range(a-i):
      print(" ",end='')

    #right star
    print("*",end='')

    print()
# bottom star
print(" "*(a+1),end='')
print("*")


