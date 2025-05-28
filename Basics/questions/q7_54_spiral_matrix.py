"""April 9, 2025

54. Spiral Matrix

Given an m x n matrix, 
return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""
"""matrix=[]
while True:
    nums = input("Enter numbers separated by commas(or enter done): ")
    if nums.lower() == 'done':
        break
    nums = list(map(int, nums.split(",")))
    matrix.append(nums)
print(matrix)"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]

#get to know the mxn
m = len(matrix[0]) #number of columns
n = len(matrix) #number of rows
"""print("m = ",m)
print("n = ",n)"""

result=[]

#setting row and column at the start
row = 0
column = 0

#setting top, bottom, left, right

#len(matrix) is the number of rows
top, bottom = 0, len(matrix)-1

#len(matrix[0]) is the number of columns
#checks how many items on [1,2,3]
left, right = 0, len(matrix[0])-1

# goes in spiral
while top <= bottom and left <= right:
    #going right
    for column in range(left,right+1):
        result.append(matrix[top][column])
    # completed the top most row
    top +=1

    #going down
    for row in range (top,bottom+1):
        result.append(matrix[row][right])
    # completed the right most column
    right -=1

    #going left
    if top <= bottom:
        for column in range(right,left-1,-1):
            result.append(matrix[bottom][column])
        # completed the bottom most row
        bottom -=1

    #going up
    if left <= right:
        for row in range (bottom,top-1,-1):
            result.append(matrix[row][left])
        # completed the left most column
        left+=1

print(result)
