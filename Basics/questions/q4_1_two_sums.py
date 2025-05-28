"""April 4, 2025

1. Two Sum
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

"""

"""nums = input("Enter numbers separated by commas: ")
nums = list(map(int, nums.split(",")))"""

nums = [2,7,11,15]

"""target = int(input("Enter the target sum: "))
"""

target = 17

#using i as the index, start at index 0 
for i in range (len(nums)):
    for j in range (i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print(i,j)
        