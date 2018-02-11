# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    
    def __str__(self):
        return str(self.start)+" "+str(self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if(len(intervals) == 0): return intervals
        
        intervals.sort(key=lambda tup:tup.start)
        
        result = [intervals[0]]
        for i in xrange(1, len(intervals), 1):
            prev = result[-1]
            current = intervals[i]
            if(current.start <= prev.end):
                prev.end = max(current.end, prev.end)
            else:
                result.append(current)
        return result


a = Solution()
k = a.merge([Interval(1, 3), Interval(2, 6),Interval(8, 10), Interval(15, 18)])
print(k)