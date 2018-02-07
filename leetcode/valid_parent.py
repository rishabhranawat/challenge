class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        stack3 = 0
        
        for i in range(0, len(s), 1):
            each = s[i]
            if(each == ")"):
                stack2.append((each, i))
            elif(each == "(" or each == "*"):
                stack1.append((each, i))
        
        if(len(stack2) > len(stack1)): return False
        else:
            while(stack1 and stack2):
                s1, s1when = stack1.pop(0)
                s2, s2when = stack2.pop(0)
                print(s1, s2)
                if(s1 == "(" and  s2 == ")" and (s1when < s2when)):
                    pass
                elif(s1 == "*" and s2 == ")" and (s1when < s2when)):
                    stack3 += 1
                else:
                    return False

        print(stack1)
        while(len(stack1) > 0):
            if(stack1.pop()[0] != "*" and stack3 <= 0):
                return False
            else:
                stack3 -= 1

        return True
       
            
a = Solution()
print(a.checkValidString("(*()"))