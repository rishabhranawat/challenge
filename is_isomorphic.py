class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping_t = {}
        mapping_s = {}
        for i in range(0, len(t), 1):
            val_t = t[i]
            val_s = s[i]
            if(val_t in mapping_t):
                if(mapping_t[val_t] != val_s): return False
            elif(val_s in mapping_s):
                if(mapping_s[val_s] != val_t): return False
            else:
                mapping_t[val_t] = val_s
                mapping_s[val_s] = val_t
        return True
a = Solution()
print(a.isIsomorphic("ab", "aa"))