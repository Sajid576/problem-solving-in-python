'''https://leetcode.com/problems/3sum/'''

import myTest
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    print("lol")
    if(len(nums) < 3):
        return []

    result = []
    nums.sort()

    for i, a in enumerate(nums):
        l = i+1
        r = len(nums)-1
        while(l < r):
            threeSum = a+nums[l]+nums[r]
            if(threeSum > 0):
                r -= 1
            elif(threeSum < 0):
                l += 1
            else:
                result.append([a, nums[l], nums[r]])

    return result


myTest.test(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
myTest.test(threeSum([]), [])
myTest.test(threeSum([0]), [])
