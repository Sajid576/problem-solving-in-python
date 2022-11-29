from my_test import test

from typing import List


def check(x, A, B):

    tops_rotate = 0
    bottoms_rotate = 0
    for i in range(len(A)):
        if(A[i] != x and B[i] != x):
            return -1
        elif(A[i] != x):
            tops_rotate += 1
        elif(B[i] != x):
            bottoms_rotate += 1
    print(tops_rotate, bottoms_rotate)
    return min(tops_rotate, bottoms_rotate)


def minDominoRotations(tops: List[int], bottoms: List[int]) -> int:
    rotations = check(tops[0], tops, bottoms)
    if(rotations != -1 or tops[0] != bottoms[0]):
        return rotations
    else:
        return check(bottoms[0], tops, bottoms)


test(minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]), -1)
test(minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]), 2)
test(minDominoRotations([1, 2, 1, 1, 1, 2, 2, 2], [2, 1, 2, 2, 2, 2, 2, 2]), 1)
