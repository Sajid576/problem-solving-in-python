from typing import List
from my_test import test


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = {}
    for item in nums:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    new = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
    result = []
    for i in range(k):
        result.append(new[i][0])

    return result


test(topKFrequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
test(topKFrequent([1], 1), [1])
