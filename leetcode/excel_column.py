class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = ["A", "B", "C", "D", "E", "F", "G", "H", 
               "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]
        label = ""
        iteration = 0
        while(s > 0):
            div = s%26
            label += arr[div-1]
            s = (s-1)/26
        return label[::-1]

a = Solution()
print(a.titleToNumber(1))
print(a.titleToNumber(53))
print(a.titleToNumber(703))
print(a.titleToNumber(52))
print(a.titleToNumber(1))

print(a.titleToNumber(26))
