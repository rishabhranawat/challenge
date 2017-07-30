# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def __init__(self):
        self.meetingRooms = 0
        self.meetings = {}
    
    def isOverlap(self, interval1, interval2):
        print(interval1.start, interval1.end)
        print(interval2.start, interval2.end)
        if((interval1.end >= interval2.start) or (interval1.start >= interval2.end)):
            return False
        return True

    def checkRooms(self, interval):
        start = interval.start
        end = interval.end
        for key, value in self.meetings.items():
            isThereSpace = True
            for i in value:
                if(self.isOverlap(i, interval) == False):
                    isThereSpace = True
                else:
                    isThereSpace = False
            if(isThereSpace == True):
                print(interval.start, interval.end)
                return False
        return True
    
    def markTimeline(self, timeline, interval):
        if(self.checkRooms(interval)):
            self.meetingRooms += 1
            self.meetings[self.meetingRooms] = [interval]
            return True
        else:
            self.meetings[self.meetingRooms].append(interval)
        return False

    def minMeetingRooms(self, intervals):
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
            self.markTimeline(timeline, interval)
        return self.meetingRooms
        
a = Solution()

i1 = Interval(9, 14)
i2 = Interval(5, 6)
i3 = Interval(3, 5)
i4 = Interval(12, 19)

i5 = Interval(2, 7)
i6 = Interval(8, 9)
i7 = Interval(8, 9)



print(a.minMeetingRooms([i5, i6, i7]))
        