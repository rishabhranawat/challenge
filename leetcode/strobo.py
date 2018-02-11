class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        strobs = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        nu = str(num)

        # for each in nu:
        #     if(each not in strobs):
        #         return False

        rev = nu[::-1]
        for i, x in enumerate(rev):
            if(x not in strobs or nu[i] != strobs[x]):
                return False
        return True

a = Solution()
print(a.isStrobogrammatic("1"))
print(a.isStrobogrammatic("818181"))