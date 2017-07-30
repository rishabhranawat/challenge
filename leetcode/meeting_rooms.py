# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def markTimeline(self, timeline, start, end):
        for i in range(start, end, 1):
            if(timeline[i] == -1): return False
            timeline[i] = -1
        return True
        
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        max_time = -1
        for interval in intervals:
            if(interval.end > max_time):
                max_time = interval.end
            
        timeline = [0]*max_time
        for interval in intervals:
            if(self.markTimeline(timeline, interval.start, interval.end) == False): 
                return False
        return True
            
        