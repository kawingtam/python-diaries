"""April 1, 2025

217. Contains Duplicate
Input: nums = [1,2,3,1]
Output: true

"""

a = input("Enter numbers separated by commas: ")
a = a.split(",")
print(a)
dup = False

seen = set()
for i in a:
    if i in seen:
        dup = True
        break
    else:
        seen.add(i)
    dup = False

print(dup)