from typing import List


def findMin(nums: List[int]) -> int:
        
        if(len(nums)==1): 
            return nums[0] 

        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
        
            if nums[high] > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1


# Self modified problem
def findMax(nums: List[int]) -> int:
        if(len(nums)==1): 
            return nums[0]
        
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            
            if nums[mid + 1] < nums[mid]:
                return nums[mid]
            if nums[mid - 1] > nums[mid]:
                return nums[mid-1]
        
            if nums[high] > nums[mid]:  #normal case
                high = mid - 1
            else:   #abnormal case
                low = mid + 1
		
print(findMin([4,5,6,7,0,1,2]))
print(findMax([4,5,6,7,0,1,2]))