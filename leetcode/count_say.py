class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        patterns = {5:"three 1s one 2", 4:"one two two 1s", 3:"one 2 one 1", 2:"two 1s", 1: "one 1"}
        ret = None
        for key in range(5, 0, -1):
            if(n > key): 
                div = key/n
                return ((patterns[key]+" ")*(n/key)).strip()
a = Solution()
print(a.countAndSay(16))