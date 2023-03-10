
'''https://leetcode.com/problems/string-to-integer-atoi/'''
from typing import List
import google_problems.my_test as my_test


def isNumber(ch):
    if(ch >= '0' and ch <= '9'):
        return True
    else:
        return False


def myAtoi(s: str) -> int:
    if(s == ''):
        return 0
    num = ''
    neg = None
    for i in range(len(s)):
        if(s[i] == '-'):
            if(neg != None):
                return 0
            else:
                neg = True
                num = '-'+num
        if(s[i] == '+'):
            if(neg != None):
                return 0
            else:
                neg = False
        if(s[i] == '.'):
            if(isNumber(s[i+1]) == True):
                if(len(num) != 0):
                    return int(num)
                else:
                    return 0
        else:
            if(isNumber(s[i]) == True):
                num += s[i]

            else:
                if(s[i] != ' ' and len(num) == 0):
                    return 0

    try:
        num = int(num)
        if(num > 2**31):
            return 2147483648
        if(num < -2**31):
            return -2147483648
        return num
    except:
        return 0


my_test.test(myAtoi("0042"), 42)
my_test.test(myAtoi("+1"), 1)
my_test.test(myAtoi("-"), 0)
my_test.test(myAtoi("-+12"), 0)
my_test.test(myAtoi("42"), 42)
my_test.test(myAtoi("       -42"), -42)
my_test.test(myAtoi("4193 with words"), 4193)
my_test.test(myAtoi("words and 987"), 0)
my_test.test(myAtoi("-91283472332"), -2147483648)
my_test.test(myAtoi("3.1416"), 3)
