# method-1: Sorting and two pointers technique

def hasArrayTwoCandidates(A, sum):
     
    # sort the array
    A.sort()
    l = 0
    r = len(A)-1
     
    # traverse the array for the two elements
    while l<r:
        if (A[l] + A[r] == sum):
            return [l,r]
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    return []
 
## method-2: hashing
def twoSum(nums, target):
        values = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in values:
                return [ values[diff],i]
            values[num] = i
        return []

 
 
# Driver program to test the functions
A = [1, 4, 45, 6, 10, -8]
n = 16
#resList=hasArrayTwoCandidates(A, n)
resList=twoSum(A,n)
if(len(resList)!=0):
    print(resList)
else:
    print("No two sum solution")   

