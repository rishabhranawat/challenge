class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        counter = {}
        for s in strs:
            if(s == ""): return ""
            for i in range(0, len(s)+1, 1):
                sg = str(s[0:i])
                if(sg in counter):
                    counter[sg] += 1
                else:
                    counter[sg] = 1
        m = ""
        for pre, count in counter.items():
            if(len(pre) > len(m) and counter[pre] == len(strs)):
                m = pre
        return m
        
a = Solution()
print(a.longestCommonPrefix(["abv", "ab", "abcd"]))
print(a.longestCommonPrefix(["a"]))