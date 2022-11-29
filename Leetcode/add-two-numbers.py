
# https://leetcode.com/problems/add-two-numbers/

from typing import List, Optional

import google_problems.my_test as my_test


def convertListToSingleNumber(mylist):
    strings = [str(integer) for integer in mylist]
    a_string = "".join(strings)
    an_integer = int(a_string)
    return an_integer


def convertSingleNumberToList(myNumber):
    myList = []
    if(myNumber == 0):
        myList.append(0)
        return myList
    else:
        while(myNumber != 0):
            rem = myNumber % 10
            myList.append(rem)
            myNumber = myNumber//10
        return myList


def addTwoNumbers(l1: Optional[List], l2: Optional[List]) -> Optional[List]:
    l1 = l1[::-1]
    l2 = l2[::-1]
    num1 = convertListToSingleNumber(l1)
    num2 = convertListToSingleNumber(l2)
   # print(num1,num2)
    res = num1+num2
    mylist = convertSingleNumberToList(res)
    return mylist


my_test.test(addTwoNumbers([2, 4, 3], [5, 6, 4]), [7, 0, 8])
my_test.test(addTwoNumbers([0], [0]), [0])
my_test.test(addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [
             9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1])
