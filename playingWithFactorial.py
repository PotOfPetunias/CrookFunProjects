import math
nums = list(reversed(range(1,13)))
##
##total = 0
##for j in nums:
##    tempSum = 1
##    for i in range(len(nums)-j):
##        tempSum = tempSum*nums[i]
##    print(tempSum, j)
##    print(tempSum/math.factorial(j))
        
f12 = math.factorial(12)
total = 0
for i in nums:
    total += f12/(math.factorial(i)*math.factorial(12 - i))
print(total)
