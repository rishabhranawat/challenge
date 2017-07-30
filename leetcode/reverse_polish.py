class Solution(object):
    def perform(self, num1, num2, op):
        if(op == "/"):
            return num1/num2
        elif(op == "*"):
            return num1*num2
        elif(op == "+"):
            return num1+num2
        else:
            return num1-num2

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """


        