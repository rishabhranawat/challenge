class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        l = list(s)
        for i in range(n-1, -1, -1):
            l[i] = s[n-1-i]
        return "".join(l)
    # O(N)

    def reverseString(self, s):
        n = len(s)
        l = list(s)
        for i in range(0, n/2, 1):
            temp = l[i]
            l[i] = l[n-1-i]
            l[n-1-i] = temp
        return "".join(l)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        l = list(s)
        for i in range(0, n/2, 1):
            temp = l[i]
            l[i] = l[n-1-i]
            l[n-1-i] = temp
        return "".join(l)
# hello
# n = 5
# n/2 = 2
# 0, 4
# 1, 3

