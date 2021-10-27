import math
from typing import List
import myTest

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





myTest.myTest(findMedianSortedArrays([2, 3], [1])  ,2 )
myTest.myTest(findMedianSortedArrays([2, 3], [1])  ,3 )
myTest.myTest(findMedianSortedArrays([2, 3], [1])  ,4 )