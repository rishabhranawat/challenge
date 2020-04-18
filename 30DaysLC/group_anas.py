class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedToAnas = {}
        for each in strs:
            v = "".join(sorted(each))

            if(v not in sortedToAnas):
                sortedToAnas[v] = []
            sortedToAnas[v].append(each)
        
        return [x for x in sortedToAnas.values()]
a = Solution()
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))