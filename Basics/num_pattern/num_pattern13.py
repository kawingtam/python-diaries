"""April 2, 2025

number spiral 

input = 5
prints:
1   2   3   4   5
16  17  18  19  6
15  24  25  20  7
14  23  22  21  8
13  12  11  10  9

"""

a = int(input("Enter a number: "))
a_square = a**2

result=[]
<<<<<<< HEAD
=======
result = [[0] * a for num in range(a)]
>>>>>>> e5a847b000f78f15598cc0723da5d070fcb8e2f2

<<<<<<< HEAD
row, column = a,a
=======
>>>>>>> e5a847b000f78f15598cc0723da5d070fcb8e2f2

<<<<<<< HEAD
top = 0
bottom = row - 1
left = 0
right = column - 1
=======
row = a
column = a
>>>>>>> e5a847b000f78f15598cc0723da5d070fcb8e2f2

<<<<<<< HEAD
=======
top = 0
bottom = row - 1
left = 0
right = column - 1
>>>>>>> e5a847b000f78f15598cc0723da5d070fcb8e2f2

<<<<<<< HEAD
=======
count = 1

while top <= bottom and left <= right:
    # go right
    for i in range (left, right+1):
        result[top][i] = count
        count += 1
    top +=1
    
    # go down
    for j in range (top, bottom+1):
        result[j][right]=count
        count+=1
    right -=1

    # go left
    if top <= bottom:
        for k in range(right,left-1,-1):
            result[bottom][k]=count
            count+=1
        bottom -=1

    # up
    if left <= right:
        for l in range (bottom,top-1,-1):
            result[l][left]=count
            count +=1
        left += 1
    
print(result)


>>>>>>> e5a847b000f78f15598cc0723da5d070fcb8e2f2
"""
# goes in spiral
while top <= bottom and left <= right:
    #going right
    for column in range(left,right+1):
        result.append(matrix[top][column])
    top +=1

    #going down
    for row in range (top,bottom+1):
        result.append(matrix[row][right])
    right -=1

    #going left
    if top <= bottom:
        for column in range(right,left-1,-1):
            result.append(matrix[bottom][column])
        bottom -=1

    #going up
    if left <= right:
        for row in range (bottom,top-1,-1):
            result.append(matrix[row][left])
        left+=1
"""

