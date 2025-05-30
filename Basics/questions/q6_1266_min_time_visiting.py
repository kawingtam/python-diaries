"""April 9, 2025

1266. Minimum Time Visiting All Points

On a 2D plane, 
there are n points with integer coordinates points[i] = [xi, yi]. 
Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units 

Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is 
[1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]  

Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
"""
nums = input("Enter numbers separated by commas: ")
nums = list(map(int, nums.split(",")))

#create list within list
points = []
for i in range(0,len(nums),2):
    x=nums[i]
    y=nums[i+1]
    points.append([x,y])
print(points)

result = 0
for i in range(0,len(points)-1):

    x1,y1=points[i]
    x2,y2=points[i+1]

    #by finding the maximum of either x or y coordinates difference
    #it will give the shortest distance to move to the next point
    #allowed to move vertically, horizontally and diagonally by 1 unit
    result += max(abs(x2-x1),abs(y2-y1))

print(result)



