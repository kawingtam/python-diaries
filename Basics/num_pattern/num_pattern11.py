"""April 2, 2025

 hill triangle, with increasing and decreasing numbers 

input = 5
prints:
$$$1
$$121
$1234321
123454321
"""

a = int(input("Enter a number: "))

for i in range (a):
    #decreasing space
    for j in range (a-i):
        print("$",end='')

    #increasing number - left
    count1 = 1
    for j in range (i+1):
        
        print(count1,end='')
        count1 +=1
    
    #decreasing number - right
    count2 = 1
    for j in range (i):
        print(count2,end='')
        count2 +=1


    print()
