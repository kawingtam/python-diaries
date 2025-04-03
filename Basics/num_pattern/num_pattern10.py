"""April 2, 2025

increasing triangle, with decreasing numbers 

input = 5
prints:
54321
$4321
$$321
$$$21
$$$$1
"""
a = int(input("Enter a number: "))
b = a
for i in range (a):
    count = b
    #increasing space
    for j in range(i+1):
        print("*",end='')

    #increasing number
    for j in range (i,a):
        
        print(count,end='')
        count -=1

       
    b -=1

    print()