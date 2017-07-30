class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s) == 0): return True
        s = list(s)
        start = 0
        end = len(s)-1
        while(start < end):
            val1 = s[start]
            val2 = s[end]
            if(val1.isalnum() and val2.isalnum()):
                if(val1.lower() != val2.lower()): return False
                else:
                    start += 1
                    end -= 1
            else:
                if(not val1.isalnum()): start += 1
                if(not val2.isalnum()): end -= 1
        return True
a = Solution()
print(a.isPalindrome("A man, a plan, a canal: Panama"))
print(a.isPalindrome("race a car"))