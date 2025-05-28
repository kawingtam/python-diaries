"""April 1, 2025

268. Missing Number
Input: nums = [3,0,1]
Output: 2

"""

"""a = input("Enter numbers separated by commas: ")

# Convert input to a list of integers
a = list(map(int, a.split(",")))"""

a = [3,4,0,1]

a_len = len(a)

for i in range(a_len+1):

    if i not in a:
        print(i)