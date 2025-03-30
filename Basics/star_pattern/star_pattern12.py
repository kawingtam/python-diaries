"""March 29, 2025

⁠Inverted Pyramid 
user enter 4
prints:
*******
 *   *
  * *
   *
"""
a = int(input("Enter a number: "))
firstline = a*2-1
#first line stars
print("*"*firstline)

for i in range (a-2):

    #increasing space
    for j in range(i+1):
        print(" ",end='')
    
    #left star
    print("*",end='')

    #middle decreasing space
    for j in range(a-2-i):
      print("$",end='')

    # print decreasing space - right
    for j in range(a-3-i):
      print("1",end='')

    #right star
    print("*",end='')

    print()

#bottom star
bottomspace = firstline // 2
print('s'* bottomspace,end='')
print("*")