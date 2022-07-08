
from typing import List


def solve(N: int, a: int, x: List[int]) -> int:
    largest = second = -2454635434
    largest_indx = -1
    # Find the largest element
    for i in range(0, N):
        if(largest < x[i]):
            largest = x[i]
            largest_indx = i

    # Find the second largest element
    for i in range(0, N):
        if(second < x[i] and i != largest_indx):
            second = x[i]

    return abs(largest-a)+abs(second-a)


print(solve(2, 1, [4, 5]))
print(solve(4, 2, [10, 4, 2, 17]))
print(solve(9, 1, [3, 10, 10, 6, 5, 3, 7, 5, 1]))
