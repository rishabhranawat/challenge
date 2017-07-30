class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = set()
        cont = True
        new = n
        while(cont):
            new_s = str(n)
            hap = 0
            for each in new_s:
                hap += int(each)**2
            n = hap
            if(n == 1): return True
            if(n in a): return False
            else: a.add(n)
        return False
a = Solution()
a.isHappy(19)