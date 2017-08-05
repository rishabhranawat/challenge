class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        counter = 0
        ret = 0
        while(counter < len(s)):
            indi = 26-(90-ord(s[counter]))
            nex = 26**counter-1
            ret += (indi + nex)
            counter += 1
        return ret
a = Solution()
print(a.titleToNumber("AAAD"))