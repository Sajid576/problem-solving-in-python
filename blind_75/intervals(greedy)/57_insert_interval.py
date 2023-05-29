from typing import List

def insert( intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

    result=[]


    for i in range(len(intervals)):
        # add non-overlapping intervals before new_interval to res
        if(intervals[i][1] < newInterval[0]):
            result.append(intervals[i])
        
        elif(intervals[i][0] > newInterval[1]):
            result.append(newInterval)
            return result + intervals[i:]

        else:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])

    result.append(newInterval)

    return result

print(insert([[1,3],[6,9]],[2,5]))