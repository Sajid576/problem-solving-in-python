

lst = list(map(int,input().strip().split(' ')))
print(lst)
x = sum(lst)
print (x-(max(lst)),end=' ')
print(x-(min(lst)))

'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly (n-1) of the n integers. 
Example:- 1,3,5,7,9 
output: 16 24

The minimum sum is  and the maximum sum is 
'''