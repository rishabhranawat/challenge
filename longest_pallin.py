class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters_count = {}
        for letter in s:
            if(letter in letters_count):
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1
        
        ret = ""
        oner = 0
        for letter, count in letters_count.items():
            while(count >= 2 and count != 0):
                ret += letter
                ret += letter
                count -= 2
            if(count > 0 and oner == 0):
                ret += letter
                oner += 1
        return len(ret)
a = Solution()
print(a.longestPalindrome("abccccdd"))
