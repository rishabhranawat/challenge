class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(haystack == needle): return 0
        if(len(needle) == 0 and len(haystack) != 0): return 0

        index = 0
        jump = len(needle)
        while(index + jump <= len(haystack)):
            print(haystack[index:index+jump])
            if(haystack[index:index+jump] == needle): return index
            index += 1
        return -1
a = Solution()
print(a.strStr("mississippi", "issi"))