# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "["+str(self.start)+", "+str(self.end)+"]"

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        for i in range(0, len(intervals), 1):
            current = intervals[i]
            if(current == None): continue
            for j in range(0, len(intervals), 1):
                check = intervals[j];
                if(i == j or check == None): continue
                if(current.start <= check.start and check.start <= current.end):
                    if(current.end < check.end):
                        current.end = check.end
                    intervals[j] = None
                elif(check.start < current.start and current.start < check.end):
                    current.start = check.start
                    if(check.end > current.end):
                        current.end = check.end
                    intervals[j] = None
                    
        ret = []
        for each in intervals:
            if(each != None and each not in ret): ret.append(each)
        return ret
a = Solution()
k = a.merge([Interval(1, 4), Interval(0, 5)])

for each in k:
    print(str(each))

