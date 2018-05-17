# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        intervals.append(newInterval)

        intervals.sort(key = lambda x:x.start)
        results = [intervals[0]]
        for i in range(1, len(intervals)):
            prev, current = results[-1], intervals[i]
            if current.start <= prev.end:
                prev.end = max(prev.end, current.end)
            else:
                results.append(current)
        return results
  
