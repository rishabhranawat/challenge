class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minElements = []
        self.elements = []
        self.currMin = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.elements.append(x)
        if(x < self.currMin or self.currMin == None):
            self.currMin = x
            self.minElements.append(x)
        else:
            self.minElements.append(self.currMin)
        

    def pop(self):
        """
        :rtype: void
        """
        self.elements.pop()
        self.minElements.pop()
        if(len(self.minElements) > 0):
            self.currMin = self.minElements[-1]
        else:
            self.currMin = None
        

    def top(self):
        """
        :rtype: int
        """
        return self.elements[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.currMin


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()