class Solution(object):
    def getNumber(self, num):
        convs = {"0":0, "1": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        mult = 10**(len(num)-1)
        val = 0
        for i in range(0, len(num), 1):
            val += (mult*convs[num[i]])
            mult /= 10
        return val
        
    
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(self.getNumber(num1)*self.getNumber(num2))
        