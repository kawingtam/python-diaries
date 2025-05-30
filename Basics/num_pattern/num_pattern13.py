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


row, column = a,a

top = 0
bottom = row - 1
left = 0
right = column - 1

matrix=[]
for i in range(row):
    matrix.append([])

for i in range(0,row):
    for j in range(0,right+1):
        matrix[j].append(0)

print(matrix)

count = 1

# goes in spiral
while top <= bottom and left <= right:
    #going right
    for column in range(left,right+1):
        matrix[top][column]=count
        count+=1
    top +=1

    #going down
    for row in range (top,bottom+1):
        matrix[row][right]=count
        count+=1
    right -=1

    #going left
    if top <= bottom:
        for column in range(right,left-1,-1):
            matrix[bottom][column]=count
            count+=1
        bottom -=1

    #going up
    if left <= right:
        for row in range (bottom,top-1,-1):
            matrix[row][left]=count
            count+=1
        left+=1

print(matrix)