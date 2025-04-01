"""April 1, 2025

448. Find All Numbers Disappeared in an Array
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

"""

a = input("Enter numbers separated by commas: ")

# Convert input to a list of integers
a = list(map(int, a.split(",")))

seen = []
missing_num = []

for i in a:
    if i in a:
        seen.append(i)
    else:
        missing_num.append(i)

missing_num.sort()
print(missing_num)