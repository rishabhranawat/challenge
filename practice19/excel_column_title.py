class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        pos = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7:"G", 8:"H",
              9:"I", 10:"J", 11:"K", 12:"L", 13:"M", 14:"N", 15:"O", 16:"P",
              17:"Q", 18:"R", 19:"S", 20:"T", 21:"U", 22:"V", 23:"W", 24:"X",25:"Y",
              26:"Z", 0:"Z"}
        
        title = ""
        while(n > 26):
            og = n//26
            v = 0
            if(og > 26):
                v = og % 26
            else:
                v = og 
            title += pos[v]
            n -= og*26

        title += pos[n]
            
        return title
a = Solution()
print(a.convertToTitle(1))
print(a.convertToTitle(701))
print(a.convertToTitle(28))
print(a.convertToTitle(1299))