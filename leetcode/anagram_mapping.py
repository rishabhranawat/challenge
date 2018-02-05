class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        mapping = {}
        for each in A:
            mapping[each] = []
        
        for i in range(0, len(B), 1):
            mapping[B[i]].append(i)
        
        map_arr = []
        
        for i in range(0, len(A), 1):
            ind = mapping[A[i]].pop()
            map_arr.append(ind)
        return map_arr
a = Solution()
print(
    a.anagramMappings([12, 28, 46, 32, 50], 
        [50, 12, 32, 46, 28]))