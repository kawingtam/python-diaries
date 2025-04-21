"""April 21, 2025
Transposing a matrix

Answer
[12, 4, 3]
[7, 5, 8]

See here the trick is that the row values move to the columns
Transposing a matrix video on Youtube for more: 
https://www.youtube.com/watch?v=TZrKrNVhbjI&ab_channel=KhanAcademy"""

x = [[12,7],
    [4 ,5],
    [3 ,8]]

m = len(x)
n = len(x[0])
print("row of x: ",m)
print("column of y: ",n)

result=[]
for i in range(n):
    result.append([])
for item in result:
    for j in range(m):
        item.append(0)

for i in range(n):
    for j in range(m):
        result[i][j] = x[j][i]
print("result : ",result)

