class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        
        if(len(s) == 0): return ret
        
        chars = {}
        for letter in p:
            if(letter in chars):    
                chars[letter] += 1
            else:
                chars[letter] = 1
        
        left = 0
        right = 0
        count = len(p)
        
        s = list(s)
        while(right < len(s)):
            leftVal = s[left]
            rightVal = s[right]

            print(left, right, count)

            if(rightVal in chars):
                if(chars[rightVal] >= 1):
                    count -= 1
                chars[rightVal] -= 1
            right += 1
            
            if(count == 0): ret.append(left)

            if(right - left == len(p)):
                if(leftVal in chars):
                    if(chars[leftVal] >= 0):
                        count += 1
                    chars[leftVal] += 1
                left += 1
        return ret
a = Solution()
print(a.findAnagrams("cbaebabacd", "abc"))
