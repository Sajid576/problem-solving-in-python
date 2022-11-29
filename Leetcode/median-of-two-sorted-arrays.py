'''https://leetcode.com/problems/median-of-two-sorted-arrays/'''

import math
from typing import List
import google_problems.my_test as my_test


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums = [*nums1, *nums2]
    nums.sort()
    # print(nums)
    if(len(nums) % 2 == 0):
        indx1 = len(nums)//2 - 1
        indx2 = len(nums)//2
        val = (nums[indx1]+nums[indx2])/2
        return val

    else:
        indx = math.floor(len(nums)/2)
        return nums[indx]


my_test.test(findMedianSortedArrays([2, 3], [1]), 2)
