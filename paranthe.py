class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s) % 2 !=0): return False

        starters = ['(', '{', '[']
        enders = [')', '}', ']']
        pairs = {'(':')', '{': '}', '[':']', ')': '(', '}':'{', ']':'['}
        s = list(s)
        index = 0
        l = []
        while(index < len(s)):
            k = s[index]
            if(k in starters):
                l.append(k)
            else:
                if(len(l) == 0): return False
                last_starter = l.pop()
                if(pairs[last_starter] != k):
                    return False
            index += 1
        if(len(l) >0): return False
        return True

a = Solution()
print(a.isValid("(([]){})"))

