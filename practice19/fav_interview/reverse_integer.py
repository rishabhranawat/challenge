class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x == 0):
            return 0
        isMinus = x < 0
        reverStr = "".join(reversed(str(abs(x)).strip("0")))
        
        x = int(reverStr)
        
        if(x > 2**31 - 1 or x < -2**31):
            return 0
        
        if(isMinus):
            x = x * -1
        return x