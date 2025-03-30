"""March 29, 2025

incresing pyramid with decreasing numbers
input = 3
prints:
1
22
333
"""
a = int(input("Enter a number: "))
for i in range(a):
    for j in range(i+1):
        print(i+1,end='')
    print()
