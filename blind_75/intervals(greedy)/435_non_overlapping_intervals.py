
from typing import List


def eraseOverlapIntervals( intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])

    result = [intervals[0]]

    for i in range(1,len(intervals)):
        if(result[-1][1]<=intervals[i][0]):
            result.append(intervals[i])

    
    return  len(intervals) - len(result)

print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))