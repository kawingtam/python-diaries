"""March 29, 2025

increasing pyramid with decreasing numbers
input = 3
prints:
3
22
111
"""

a = int(input("Enter a number: "))
count = a
for i in range(a):
    for j in range(i+1):
        print(count,end='')
    count -= 1
    print()
