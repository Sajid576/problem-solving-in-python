'''https://leetcode.com/problems/3sum/'''

import myTest
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:

    if(len(nums) < 3):
        return []

    result = []
    nums.sort()

    for i in range(len(nums)):
        l = i+1
        r = len(nums)-1
        while(l < r):
            threeSum = nums[i]+nums[l]+nums[r]
            if(threeSum > 0):
                r -= 1
            elif(threeSum < 0):
                l += 1
            else:
                if([nums[i], nums[l], nums[r]] not in result):
                    result.append([nums[i], nums[l], nums[r]])
                l += 1

    return result


myTest.test(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
myTest.test(threeSum([]), [])
myTest.test(threeSum([0]), [])
