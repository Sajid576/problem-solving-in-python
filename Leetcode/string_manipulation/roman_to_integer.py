'''https://leetcode.com/problems/roman-to-integer/'''


from typing import List
import google_problems.my_test as my_test


def romanToInt(s: str) -> int:
    symToVal = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    num = ''
    if(s in symToVal):
        return symToVal[s]

    for i in range(len(s)):
        if(s[i] in symToVal):

            symToVal[s[i]]

    return int(num)


my_test.test(romanToInt("I"), 1)
my_test.test(romanToInt("III"), 3)
my_test.test(romanToInt("IV"), 4)
my_test.test(romanToInt("IX"), 9)
my_test.test(romanToInt("LVIII"), 58)
my_test.test(romanToInt("MCMXCIV"), 1994)
