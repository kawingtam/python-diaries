"""April 2, 2025

increasing triangle, with decreasing numbers 

input = 5
prints:
5
54
543
5432
54321
"""
a = int(input("Enter a number: "))

for i in range (a):
    count=a
    for j in range (i+1):
        
        print(count,end='')
        count-=1

    print()