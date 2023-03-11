from typing import List


def search(nums: List[int], target: int) -> int:
        if not nums: return -1
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[hi]: # normal case
                if target >= nums[mid] and target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
            else:   # rotated case/abnormal case
                if target >= nums[lo] and target <= nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
        return -1
		
print(search([4,5,6,7,0,1,2],0))