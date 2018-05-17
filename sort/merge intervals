# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        '''
        init_len = len(intervals)
        
        
        for j in range(4):
            i = 0
            
            while i < init_len - 1:
                k = i + 1
                while k < init_len:
                    if intervals[i].end >= intervals[k].start and intervals[i].start <= intervals[k].end:

                        intervals[i].end = max(intervals[i].end, intervals[k].end)
                        intervals[i].start = min(intervals[k].start, intervals[i].start)

                        del intervals[k]
                        init_len -= 1
                        
                    k += 1
                i += 1
            
        return intervals
        '''以上有bug（运行时间慢将循环改成list总长）
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end:
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
        return result
