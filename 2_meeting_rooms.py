# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    
    def checkMeetings(self, meetings, interval):
        for key, value in meetings.items():
            isThereSpaceSlot = True
            for subInterval in value:
                if(not ((interval.start >= subInterval.end) or (interval.end <= subInterval.start))):
                    print(str(interval.start) +">=" +str(subInterval.end))
                    print(str(interval.end) + "<="+ str(subInterval.start))
                    return True
            if(isThereSpaceSlot): return False
        return False
    
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        meetings = {}
        nmeetings =0
        for interval in intervals:
            if(self.checkMeetings(meetings, interval)):
                nmeetings += 1
                meetings[nmeetings] = [interval]
            else:
                if(nmeetings == 0):
                    nmeetings += 1
                    meetings[nmeetings] = [interval]
                else:
                	meetings[nmeetings].append(interval)

        return nmeetings

a = Solution()
i1 = Interval(1, 17)
i2 = Interval(7, 10)
i3 = Interval(12, 14)

print(a.minMeetingRooms([i1, i2, i3]))