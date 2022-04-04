'''https://leetcode.com/problems/ugly-number/'''

from typing import List
import google_problems.my_test as my_test


def isUgly(n: int) -> bool:
    if(n == 0):
        return False
    while n % 2 == 0:
        n = n / 2
    while n % 3 == 0:
        n = n / 3
    while n % 5 == 0:
        n = n / 5

    if(n != 1):
        return False
    else:
        return True


my_test.test(isUgly(6), True)
my_test.test(isUgly(8), True)
my_test.test(isUgly(14), False)
my_test.test(isUgly(1), True)
