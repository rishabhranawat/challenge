class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        for each in wordDict:
            if(each in s):
                s = s.replace(each, "")
        return len(s) == 0
a = Solution()
print(a.wordBreak("aaaaaaa", ["aaaa","aa"]))