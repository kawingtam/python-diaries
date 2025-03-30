"""March 29, 2025

single number pattern
input = 3
prints:
1
11
111
"""
a = int(input("Enter a number: "))

for i in range(a):
    for j in range(i+1):
        print("1",end='')
    print()