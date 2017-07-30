class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        counter = 0
        minutes = []
        while(counter < len(timePoints)):
            val = timePoints[counter]
            if(val == "00:00"):
                timePoints[counter] = "24:00"
            if(val.split(":")[1] == "00"):
                val = val.replace()
            k = .replace(":", ".")
            kl = k.split(".")
            tots = float(kl[0])*60+float(kl[1])
            minutes.append(tots)
            counter += 1

        s = sorted(minutes)
        print(minutes)
        minDiff = 10000000
        for i in range(0, len(minutes)-1, 1):
            k1 = s[i]
            k2 = s[i+1]
            print(k2, k1)
            if(k2 - k1 < minDiff):
                minDiff = k2 - k1
        return minDiff

        
a = Solution()
print(a.findMinDifference(["05:31","22:08","00:35"]))