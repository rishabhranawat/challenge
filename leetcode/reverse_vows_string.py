class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vows = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        inds = []
        s = list(s)
        for i in range(0, len(s), 1):
            if(s[i] in vows): 
                inds.append(i)
        
        start = 0
        end = len(inds)-1
        if(start == end): return "".join(s)
        
        while(start < end):
            temp = s[inds[start]]
            s[inds[start]] = s[inds[end]]
            s[inds[end]] = temp
            start += 1
            end -= 1
        ret = "".join(s)
        return ret
        
            
        
            