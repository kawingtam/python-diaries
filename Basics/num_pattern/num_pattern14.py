"""April 21, 2025
Multiply 2 matrices
# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

Answer = [114, 160, 60, 27]
[74, 97, 73, 14]
[119, 157, 112, 23]

Note that given matrix 1 size is m*n and matrix 2 size is n*p
I.e., the number of rows in matrix 1 must match number of rows in matrix 2"""
matrix1=[]
while True:
    nums = input("Matrix1: Enter numbers separated by commas(or enter done): ")
    if nums.lower() == 'done':
        break
    nums = list(map(int, nums.split(",")))
    matrix1.append(nums)

matrix2=[]
while True:
    nums = input("Matrix2: Enter numbers separated by commas(or enter done): ")
    if nums.lower() == 'done':
        break
    nums = list(map(int, nums.split(",")))
    matrix2.append(nums)

print(matrix1)
print(matrix2)