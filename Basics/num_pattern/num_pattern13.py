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
#setting row and column
row = 0
column = 0

#setting top, bottom, left, right
top, bottom = 0, a-1
left, right = 0, a-1

for i in range (a_square+1):
    while top <= bottom and left <= right:
        #going right
        for i in range(left,right+1):
            result.append(i)
        top +=1

        #going down
        for i in range(top,bottom+1):
            result.append(i)
        bottom+=1

print(result)


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

