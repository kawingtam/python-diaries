"""April 2, 2025

number spiral 

input = 5
prints:
1   2   3   4   5
16  17  18  19  6
15  24  25  20  7
14  23  22  21  8
13  12  11  10  9

Accessing elements using indexing
matrix[row, column]

Update matrix row
matrix[1, :] = [11, 12, 13]

Update matrix column
matrix[:, 2] = [14, 15, 16]
"""


a = int(input("Enter a number: "))
matrix = [[0]*a for i in range (a)]
#Right, Down, Left, Up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Start by moving "Right"
current_direction = 0  

# Starting position
row, col = 0, 0  

for i in range(a):
    row += directions[current_direction][0]
    print(row)
    col += directions[current_direction][1]
    print(col)
    print() 

"""    if i % 3 == 2:  
        # Cycle through 0 → 1 → 2 → 3 → 0
        current_direction = (current_direction + 1) % 4  """