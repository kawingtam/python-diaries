"""April 2, 2025

increasing triangle, increasing number
Floyd triangle

input = 4
prints:
1
23
456
78910
"""

a = int(input("Enter a number: "))
count = 1
row = 1
for i in range (a):
    for j in range (row):
        print(count,end='')
        count += 1
    row +=1
    print()