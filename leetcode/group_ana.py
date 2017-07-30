class Solution(object):
    def checkInDict(self, dic, s):
        o = sorted(s)
        o = ''.join(o)
        if(o in dic):
            dic[o].append(s)
        else:
            dic[o] = [s]
        return dic
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for each in strs:
            dic = self.checkInDict(dic, each)
        ret = []
        for key, value in dic.items():
            ret.append(value)
        return ret
        
a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))