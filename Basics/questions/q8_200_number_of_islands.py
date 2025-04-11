"""April 11, 2025

200. Number of Islands

Given an m x n 2D binary grid
'1's (land) and '0's (water)
return the number of islands.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""
matrix=[]
while True:
    nums = input("Enter numbers separated by commas(or enter done): ")
    if nums.lower() == 'done':
        break
    nums = list(map(int, nums.split(",")))
    matrix.append(nums)
print('\n'.join(str(row) for row in matrix))

top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1
print(top,bottom,left,right)

island = 0 
visited = set()

