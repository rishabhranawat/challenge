class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :rtype: int
        """
        if(k == 0): return 0
        if(len(s) <= k): return len(s)

        start = 0
        nex = 1
        
        start_val = s[start]
        pairs = {}
        pairs[start_val] = 1

        ma = 0
        curr = 1
        while(nex < len(s)):
            val = s[nex]
            if(val in pairs):
                pairs[val] += 1
                curr += 1
            else:
                while(len(pairs) >= k):
                    pairs[start_val] -= 1
                    if(pairs[start_val] == 0): pairs.pop(start_val)
                    start+=1
                    start_val = s[start]
                    curr -= 1
                curr += 1
                pairs[val] = 1
            nex += 1        
            ma = max(curr, ma)
        return ma
a = Solution()
print(a.lengthOfLongestSubstringKDistinct("eceba", 3))