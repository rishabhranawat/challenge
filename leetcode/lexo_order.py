class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = map(str, list(range(1, n)))
        return map(int, sorted(output))



a = Solution()
print(a.lexicalOrder(1000))
