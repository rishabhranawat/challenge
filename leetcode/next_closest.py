class Solution(object):
    
    def diffBetweenTime(self, given_h, given_m, potential_h, potential_m):
        hours = 24-given_h
        hours = hours + potential_h

        # hours = (potential_h-given_h)
        minutes = (potential_m-given_m)
        diff = (hours*60)+minutes
        if(diff >= 1440):
            diff = diff - 1440
        return diff
        
        
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = list(time.replace(":", ""))
        ghours, gminutes = int(time.split(":")[0]), int(time.split(":")[1])
        
        diff = None
        closest = ""

        for hours in range(0, 24, 1):
            h_str = str(hours)
            if(hours < 10):
                h_str = "0" + h_str
            if(h_str[0] not in nums or h_str[1] not in nums):
                continue
            else:
                for minutes in range(0, 60, 1):
                    m_str = str(minutes)
                    if(minutes < 10):
                        m_str = "0"+m_str
                    if(m_str[0] not in nums or m_str[1] not in nums):
                        continue
                    else:
                        current_diff = self.diffBetweenTime(ghours, gminutes, hours, minutes)
                        if((diff == None or diff > current_diff) and current_diff != 0):
                            diff = current_diff
                            if(hours < 10):
                                closest = "0"+str(hours)+":"
                            else:
                                closest = str(hours)+":"
                            if(minutes < 10):
                                closest += "0"+str(minutes)
                            else:
                                closest += str(minutes)
        return closest
class Solution(object):
    def nextClosestTime(self, time):
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from datetime import datetime, timedelta
def solution(S):
    # write your code in Python 3.6
    t = datetime.strptime(S, '%H:%M')
    found = True
    digits_in_time = list(S.replace(":", ""))
    while(found):
        t = t + timedelta(minutes=1)
        digits_in_next = list(t.strftime('%H:%M').replace(":", ""))
        dg = list(S.replace(":", ""))
        valid = True
        for each in digits_in_next:
            if(each not in dg):
                valid = False
            else:
                dg.remove(each)
        if(valid): return t.strftime('%H:%M')
        print(t)
    

        
a = solution("00:00")