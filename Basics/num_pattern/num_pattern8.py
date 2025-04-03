"""April 2, 2025

increasing hill triangle, with increasing numbers 

input = 5
prints:
$$$1
$$123
$1234567
123456789
"""

a = int(input("Enter a number: "))

for i in range(a):
    count = 1

    #decreasing space
    for j in range(a-i):
        print("*",end='')
    
    #incresing number - left
    for j in range(i+1):
        print(count,end='')
        count+=1

    #incresing number - right
    for j in range(i):
        print(count,end='')
        count+=1

    print()
