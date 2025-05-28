"""April 1, 2025

448. Find All Numbers Disappeared in an Array
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

"""

"""a = input("Enter numbers separated by commas: ")
a = list(map(int, a.split(",")))"""

a = [4,3,2,7,8,2,3,1]

missing_num = []

# Check for missing numbers in the range 1 to n
for i in range(1, len(a) + 1):
    if i not in a:
        missing_num.append(i)

missing_num.sort()
print(missing_num)