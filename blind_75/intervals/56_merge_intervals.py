

from typing import List


def merge( intervals: List[List[int]]) -> List[List[int]]:

    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for i in range(1,len(intervals)):
        if(result[-1][1]>=intervals[i][0]):
            result[-1][1] = max(result[-1][1],intervals[i][1])
        else:
            result.append(intervals[i])

    return result


print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))