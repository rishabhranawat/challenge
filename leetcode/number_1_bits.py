class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = ("{0:b}".format(12456))
        k = 0
        for each in s:
        	if(each == "1"): k += 1
       	return k
a = Solution()
print(a.hammingWeight(10))