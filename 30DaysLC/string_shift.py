class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        netShift = 0
    
        for direction, amount in shift:
            if(direction == 0):
                netShift -= amount
            else:
                netShift += amount
        print(netShift, s)
        return self.shift(s, netShift)
    
    def shift(self, s, shift):
        l = [0 for x in range(0, len(s))]
        for i in range(0, len(s), 1):
            l[(i + shift)%len(s)] = s[i]
        return "".join(l)
a = Solution()
print(a.stringShift("abc", [[0,1],[1,2]]))
print(a.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))