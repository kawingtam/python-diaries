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

Answer = 
[114, 160, 60, 27]
[74, 97, 73, 14]
[119, 157, 112, 23]

Note that given matrix 1 size is m*n and matrix 2 size is n*p
I.e., the number of rows in matrix 1 must match number of rows in matrix 2"""

x = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
print(x)
print(y)
print()

m = len(x) #rows
n = len(x[0]) #columns of m1 and rows of m2
p = len(y[0]) #columns of m2

print("rows of m1(m,i): ",m)
print("columns of m1(n,k): ",n)
print("columns of m2(p,j): ",p)
print()

result = []
# i is row of x
for i in range(m):
    result.append([])

# j is column of y
for item in result:
    for j in range(p):
        item.append(0)
print(result)

# set k to column of x and row of y

for i in range(m):
    for j in range(p):
        for k in range (n):
            result[i][j]+=x[i][k]*y[k][j]

print(result)
