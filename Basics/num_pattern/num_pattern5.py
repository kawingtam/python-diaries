"""April 1, 2025

diamond pattern, with increasing numbers 

input = 5
prints:
$$$$1$$$$
$$$222$$$
$$33333$$
$4444444$
555555555
$6666666$
$$77777$$
$$$888$$$
$$$$9$$$$
"""

a = int(input("Enter a number: "))
count = 1

#upper
for i in range(a):
    #decreasing space - left
    for j in range (a-1-i):
        print("$",end='')

    #increasing nums - left
    for j in range(i+1):
        print(count,end='')

    #increasing nums - right
    for j in range(i):
        print(count,end='')

    count +=1

    print()

#lower
for i in range(a):
    #increasing space - left
    for j in range (i+1):
        print("$",end='')

    #increasing nums - left
    for j in range(a-1-i):
        print(count,end='')

    #increasing nums - right
    for j in range(a-2-i):
        print(count,end='')


    count +=1

    print()