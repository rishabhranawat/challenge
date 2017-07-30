class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        for each in ([2, 3, 5]):
            while(num and num % each == 0):
                num = num/each
        return num == 1
a = Solution()
print(a.isUgly(7))