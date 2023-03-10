'''https://leetcode.com/problems/reverse-integer/'''


from typing import List
import google_problems.my_test as my_test


def reverse(x: int) -> int:
    myNumber = x
    isTrailingZero = True

    if(x < 0):
        myNumber = myNumber*(-1)
    revNumber = ""
    if(myNumber == 0):
        return myNumber
    else:
        while(myNumber != 0):
            rem = myNumber % 10
            if(rem != 0):
                isTrailingZero = False
            if(isTrailingZero == False):
                revNumber += str(rem)
            myNumber = myNumber//10
        if(x < 0):
            revNumber = '-'+revNumber
        revNumber = int(revNumber)
        if(revNumber > 2**31 or revNumber < -2**31):
            return 0
        return revNumber


my_test.myTest(reverse(-123), -321)
my_test.myTest(reverse(123), 321)
my_test.myTest(reverse(120), 21)
my_test.myTest(reverse(0), 0)
my_test.myTest(reverse(1534236469), 0)
