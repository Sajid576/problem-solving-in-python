'''https://leetcode.com/problems/happy-number/'''
from typing import List
import myTest


def sumi(n):
	res = 0
	while n:
		res += (n % 10)**2
		n //= 10
	return res


def isHappy(n: int) -> bool:
	# Time and Space: O(logn), O(logn)
    res = set()
    while n != 1 and n not in res:
        res.add(n)
        n = sumi(n)

    if(n == 1):
        return True
    else:
        return False


myTest.test(isHappy(19), True)

myTest.test(isHappy(2), False)
