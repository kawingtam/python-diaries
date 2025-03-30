"""March 29, 2025

increasing pyramid with increasing numbers increment of 2
input = 3
prints:
0
22
444
"""

a = int(input("Enter a number: "))
count = 0

for i in range(a):
    for j in range(i+1):
        print(count,end='')
    count +=2
    print()
