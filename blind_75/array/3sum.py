'''https://leetcode.com/problems/3sum/'''

import google_problems.my_test as my_test
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


my_test.test(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
my_test.test(threeSum([]), [])
my_test.test(threeSum([0]), [])
