'''https://leetcode.com/problems/roman-to-integer/'''


from typing import List
import myTest


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


myTest.test(romanToInt("I"), 1)
myTest.test(romanToInt("III"), 3)
myTest.test(romanToInt("IV"), 4)
myTest.test(romanToInt("IX"), 9)
myTest.test(romanToInt("LVIII"), 58)
myTest.test(romanToInt("MCMXCIV"), 1994)
