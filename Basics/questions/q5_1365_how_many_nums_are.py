"""April 4, 2025

1365. How Many Numbers Are Smaller Than the Current Number

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
"""

nums = input("Enter numbers separated by commas: ")
nums = list(map(int, nums.split(",")))
smaller=[]
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] > nums[j]:
            count +=1
    smaller.append(count)
print(smaller)
