"""April 9, 2025

54. Spiral Matrix

Given an m x n matrix, 
return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""
matrix=[]
while True:
    nums = input("Enter numbers separated by commas(or enter done): ")
    if nums.lower() == 'done':
        break
    nums = list(map(int, nums.split(",")))
    matrix.append(nums)
print(matrix)

#get to know the mxn
m = len(matrix[0])
n = len(matrix)
print(m)
print(n)