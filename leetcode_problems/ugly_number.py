'''https://leetcode.com/problems/ugly-number/'''

from typing import List
import myTest


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


myTest.test(isUgly(6), True)
myTest.test(isUgly(8), True)
myTest.test(isUgly(14), False)
myTest.test(isUgly(1), True)
