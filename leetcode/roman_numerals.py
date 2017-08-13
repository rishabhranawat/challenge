class Solution(object):
    def getPreviousSmallest(self, num):

        ns = [1, 5, 10, 50, 100, 500, 1000]
        if(num > ns[len(ns)-1]): return 1000, 100
        margins = [0, 1, 1, 10, 10, 100, 100]
        if(num in ns): return num, margins[ns.index(num)]
        for i in range(0, len(ns)-1, 1):
            next = ns[i+1]
            next_marg = margins[i+1]
            if(num > ns[i] and num < next):
                if(next > num and (next-next_marg) <= num): return next, next_marg
                else: return ns[i], margins[i]
        return None, None

    def getConversion(self, dig):

        d = {1: "I", 5: "V", 10: "X", 50: "L", 100 : "C", 500: "D", 1000: "M"}
        ret = ""
        nearest, margin = self.getPreviousSmallest(dig)
        if(nearest == None): return ret
        diff = dig - nearest
        if(diff < 0):
            ret += d[margin]+d[nearest]
        while(diff >= 0):
            if(diff == 0):
                ret += d[nearest]
            elif(dig > nearest):
                ret += d[nearest]
            else:
                ret += d[margin]+d[nearest]
            nearest, margin = self.getPreviousSmallest(diff)
            if(nearest !=None): diff = diff - nearest
            else: diff = -1
        return ret
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        num_str = str(num)
        div = 10
        while(num > 0):
            left = num % div
            num -= left
            div *= 10
            roman = self.getConversion(left)+roman
        return roman
            

        
a = Solution()
print(a.intToRoman(578))
print(a.intToRoman(3))
print(a.intToRoman(8))
print(a.intToRoman(18))
print(a.intToRoman(2100))
print(a.intToRoman(40))