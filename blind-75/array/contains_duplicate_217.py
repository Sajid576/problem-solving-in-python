from typing import List
from my_test import test


def containsDuplicate(nums: List[int]) -> bool:
    counter = set()

    for num in nums:
        if num not in counter:
            counter.add(num)
        else:
            return True

    return False


test(containsDuplicate([1, 2, 3, 4]), False)
test(containsDuplicate([1, 2, 3, 1]), True)
