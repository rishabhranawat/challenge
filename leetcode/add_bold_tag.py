class Solution(object):
    def addBoldTag(self, s, dic):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        bolders= []
        for i, v in enumerate(dic):
            if(v in s): 
                i = 0
                while(i+len(v) <= len(s)):
                    if(s[i:i+len(v)] == v):
                        start = i
                        end = start+len(v)
                        bolders.append([start, end])
                    i += 1
        
        bolders.sort(key=lambda tup:tup[0])
        print(bolders)

        result = [bolders[0]]
        for i in xrange(1, len(bolders)):
            prev, current = result[-1], bolders[i]
            if(current[0] <= prev[1]):
                prev[1] = max(prev[1], current[1])
            else:
                result.append(current)
        bolders = result
        print(bolders)

        added = 0
        for start, end in bolders:
            start = start+added
            end = end+added
            s = s[:start]+"<b>"+s[start:end]+"</b>"+s[end:]
            added += 7

        while("</b><b>" in s):
            double_index = s.find("</b><b>")
            start = double_index
            end = double_index + 7
            s = s[:start]+s[end:]

        return s
        
        
a = Solution()
s="abcxyz123"
dict=["abc","123"]
print(a.addBoldTag(s, dict))