This folder contains the problems that appeared on  Google ,Facebook,Uber and other top most company.

- Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Do it in one pass.
Practice: https://leetcode.com/problems/two-sum/
https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/
https://dev.to/xshirl/two-sum-leetcode-3afp
i)
 Practice: https://leetcode.com/problems/max-number-of-k-sum-pairs/
https://www.geeksforgeeks.org/count-pairs-with-given-sum/
 
 
- Day-2: Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example,
 if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
 If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
https://leetcode.com/problems/product-of-array-except-self/

- Day-5: cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair



Implement car and cdr.