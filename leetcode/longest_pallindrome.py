class Solution(object):
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        while(start < end):
            if(s[start] != s[end]): return False
            start += 1
            end -= 1
        return True
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s) <= 1): return s
        
        start = 0
        nex = 1
        
        leng = 0
        ret_str = ""
        while(nex < len(s)):
            curr_str = s[start:nex+1]
            if(self.isPalindrome(curr_str)):
                if(leng < len(curr_str)):
                    ret_str = curr_str
                    leng = len(curr_str)
                nex += 1
                start += 1
            else:
                nex += 1
        return ret_str
        
a = Solution()
print(a.longestPalindrome("cbbd"))