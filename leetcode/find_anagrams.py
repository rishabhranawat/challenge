class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        index = 0
        jump = len(p)
        pairs = {}
        while(index + jump <= len(s)):
            val = s[index:index+jump]
            val = "".join(sorted(val))
            if(val in pairs):
                pairs[val].append(index)
            else:
                pairs[val] = [index]
            index += 1
        ret = "".join(sorted(p))
        if(ret in pairs): return pairs[ret]
        else: return []
        
a = Solution()
print(a.findAnagrams("abab","ab"))