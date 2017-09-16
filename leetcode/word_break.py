class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d = [False]*len(s)

        for i in range(len(s)):
            for w in wordDict:
                val = s[i-len(w)+1:i+1]
                if(w == val and (i-len(w) == -1 or d[i-len(w)])):
                    d[i] = True
                print(w, d)
        return d[-1]
a = Solution()
print(a.wordBreak("leetcode", ["leet","code"]))
print(a.wordBreak("aaaaaa", ["a","aaaaaa"]))