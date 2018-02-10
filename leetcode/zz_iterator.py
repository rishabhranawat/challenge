class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.lastCalled = 2

    def next(self):
        """
        :rtype: int
        """
        # print(self.lastCalled, self.v2, self.v1)
        if(self.lastCalled == 1):
            if(len(self.v2) > 0): 
                self.lastCalled = 2
                return self.v2.pop(0)
            else: 
                self.lastCalled = 2
                if(self.hasNext()): return self.next()
        else:
            if(len(self.v1) > 0): 
                self.lastCalled = 1
                return self.v1.pop(0)
            else:
                self.lastCalled = 1
                if(self.hasNext()): return self.next()
                
    def hasNext(self):
        """
        :rtype: bool
        """
        return (not len(self.v1) == 0 or not len(self.v2) == 0)
            
        

# Your ZigzagIterator object will be instantiated and called as such:
v1 = [1,2]
v2 = [3,4,5,6]
i, v = ZigzagIterator(v1, v2), []
while i.hasNext(): v.append(i.next())
print(v)
