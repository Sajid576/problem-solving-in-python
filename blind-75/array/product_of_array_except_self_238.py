from typing import List
from my_test import test


def productExceptSelf(nums: List[int]) -> List[int]:
    total_multiply = 1
    zero_cnt = 0
    for num in nums:
        if(num != 0):
            total_multiply *= num
        else:
            zero_cnt += 1

    result = []
    for num in nums:
        if((num != 0)):
            if(zero_cnt > 0):
                result.append(0)
            else:
                result.append(total_multiply // num)

        else:
            if(zero_cnt == 1):
                result.append(total_multiply)
            else:
                result.append(0)

    return result


test(productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
test(productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
