"""April 2, 2025

input = 5
prints:
12345
1234
123
12
1
"""

a = int(input("Enter a number: "))
for i in range (a):

    #increasing space
    for j in range (i):
        print("$",end='')

    count=1
    for j in range(a-i):
        print(count,end='')
        count+=1
    print()
    count=1
    