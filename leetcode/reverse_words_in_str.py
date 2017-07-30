class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        import re

        s = re.sub( '\s+', ' ', s ).strip()
        s = s.split(" ")
        start = 0
        end = len(s)-1
        while(start <= end):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        return " ".join(s)
a = Solution()
print(a.reverseWords("hi!"))