class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letters = {1: 'A', 2: 'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 
                   15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26:'Z'}
        
        letter_rep = []
        if(n <= 26): return letters[n]
        else:
            ret_str = ""
            while(n > 0 and n%26 != 0 and n/26 != 0):
                ret_str += letters[n/26]
                ret_str += letters[n%26]
                n /= 26
            return ret_str
a = Solution()
print(a.convertToTitle(1))
print(a.convertToTitle(26))
print(a.convertToTitle(27))
print(a.convertToTitle(52))
print(a.convertToTitle(76))