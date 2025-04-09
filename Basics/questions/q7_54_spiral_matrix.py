"""April 9, 2025

54. Spiral Matrix

Given an m x n matrix, 
return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
"""
import math
nums = input("Enter numbers separated by commas: ")
nums = list(map(int, nums.split(",")))

#create list within list
row = []
len_of_outer_matrix= len(nums)
len_of_inner_matrix=len(x) for x in nums[0]
print(len_of_inner_matrix)

for i in range(0,len(nums),3):
    x=nums[i]
    y=nums[i+1]
    z=nums[i+2]
    row.append([x,y,z])
print(row)

result = []
