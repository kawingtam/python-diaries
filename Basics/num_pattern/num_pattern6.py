"""April 2, 2025

increasing triangle, with increasing numbers 

input = 5
prints:
1
12
123
1234
12345
"""

a = int(input("Enter a number: "))
for i in range (a):
    count=1

    for j in range(i+1):
        print(count,end='')
        count+=1
    print()