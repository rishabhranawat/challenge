class Solution(object):
    def decode(self, n, sub):
        if(n == 0): return ""
        else:
            return n*self.decodeString(sub)
    
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        v = ""
        while(i < len(s)):
            char = s[i]
            if(char.isdigit()):
                start = i
                while(char.isdigit()):
                    i += 1
                    char = s[i]
                
                number = int(s[start:i])
                i += 1
                closers = 1
                sub = ""
                while(closers != 0):
                    char = s[i]
                    if(char == "["):
                        closers += 1
                        sub += "["
                    elif(char == "]"):
                        closers -= 1
                        if(closers > 0):
                            sub += "]"
                    else:
                        sub += char
                    i += 1
                v += self.decode(number, sub)
            else:
                v += char
                i += 1
        return v
                
a = Solution()
print(a.decodeString("100[leetcode]"))