from typing import List


def countBits(num: int) -> List[int]:
    results = [0]
    print(results)
    for i in range(1, num+1):
        results.append(results[i & (i-1)] + 1)

    return results


print(countBits(3))
