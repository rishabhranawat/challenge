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
                        if(minutes == 39): print(current_diff)
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

a = Solution()
a.nextClosestTime("00:00")
a.nextClosestTime("23:59")