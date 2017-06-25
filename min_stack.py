class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.mins = []
        self.minVal = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.l.append(x)
        if(self.minVal == None or self.minVal > x): 
            self.minVal = x
            self.mins.append(self.minVal)
        

    def pop(self):
        """
        :rtype: void
        """
        val = self.l[len(self.l)-1]
        if(val == self.mins[len(self.mins)-1]):
            minV = self.mins[len(self.mins)-1]
            self.mins.remove(minV)
        return self.l.remove(val)

    def top(self):
        """
        :rtype: int
        """
        return self.l[len(self.l)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[len(self.mins)-1]

        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
minStack.top()   
print(minStack.getMin())