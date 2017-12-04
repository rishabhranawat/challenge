class Parens(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pare = []
        s = [None]*(2*n)

        self.generateHelper(n, n, 0, s, pare)
        return pare
    
    def generateHelper(self, left, right, count, s, pare):
        if(left < 0 or right < left): return
        
        if(left == 0 and right == 0):
            
            pare.append("".join(s))
        else:
            if(left > 0):
                s[count] = '('
                self.generateHelper(left-1, right, count+1, s, pare)
            if(right > left):
                s[count] = ')'
                self.generateHelper(left, right-1, count+1, s, pare)
                

a = Parens()
print(a.generateParenthesis(3))