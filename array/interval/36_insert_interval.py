from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # result list
        res = []
        # iterate through the intervals
        for i in range(len(intervals)):
            #  if the new interval comes before the current interval, add the new interval. And since the intervals are sorted non-overlapping, we can add rest of the intervals as it is and return
            if (newInterval[1] < intervals[i][0]):
                res.append(newInterval)
                return res + intervals[i:]
            # if the new interval comes after the current interval, add the current interval to the result list
            elif (newInterval[0] > intervals[i][1]):
                res.append(intervals[i])
            # If non of the above conditions are met, then there is an overlap between the new interval and the current interval. So we merge the intervals.
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        # add the new interval to the result list at the end if it is not added in the loop.
        res.append(newInterval)
        return res
        