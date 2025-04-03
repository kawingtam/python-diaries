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

for i in range (a):
    print("$"*i,end='')
    count = a-i
    for j in range (a-i):
        print(count,end='')
        count -=1
    print()