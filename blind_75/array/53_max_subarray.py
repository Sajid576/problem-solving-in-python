from typing import List


def maxSubArray(nums: List[int]) -> int:
        sum=0
        ans=-10000
        
        for i in range(len(nums)):
            sum+=nums[i]
            if(sum>ans):
                ans=sum
            if(sum<0):
                sum=0
        
        return ans