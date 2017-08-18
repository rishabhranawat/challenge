class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) <= 1): return len(s)
        
        start = 0
        start_val = s[start]
        nex = 1
        chars = set()
        chars.add(start_val)
        curr = 0
        ma = 0
        while(nex < len(s)):
            val = s[nex]
            if(val not in chars):
                chars.add(val)
                curr += 1
            else:
                while(val in chars):
                    chars.remove(start_val)
                    start += 1
                    start_val = s[start]
                    curr -= 1
                chars.add(val)
            nex += 1
            ma = max(ma, len(chars))
        return ma
                
a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.lengthOfLongestSubstring("pwwkew"))
print(a.lengthOfLongestSubstring("bbbb"))