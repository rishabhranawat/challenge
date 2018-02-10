class BIT:

    def __init__(self, nums):
        self.bit = self.generate(nums)
        self.nums = nums
    
    '''
    2's complement
    AND with original
    Add to original
    '''
    def next(self, index):
        complement = (~index)+1
        return (complement&index) + index

    '''
    2's complement
    AND with original
    Subtract from original
    '''
    def parent(self, index):
        complement = (~index)+1
        return index - (complement&index)

    '''
    Generate the BIT
    '''
    def generate(self, nums):
        bit = [0]*(len(nums)+1)

        for i in range(1, len(nums)+1, 1):
            next = i
            
            while(next < len(bit)):
                bit[next] += nums[i-1]
                next = self.next(next)
        return bit

    '''
    Cumulative
    '''
    def cumulative(self, index):
        index = index + 1
        next = index
        cumu = 0
        while(next > 0):
            cumu += self.bit[next]
            next = self.parent(next)
        return cumu

    def update(self, index, value):
        diff = value - self.nums[index]
        self.nums[index] =value
        index = index + 1
        next = index
        while(next < len(self.bit)):
            self.bit[next] += diff
            next = self.next(next)
        print(index, value, self.bit)
        return True


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.bit = BIT(nums)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.bit.update(i, val)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.bit.cumulative(j)-self.bit.cumulative(i-1)
        

nums = [7, 2, 7, 2, 0]

# Your NumArray object will be instantiated and called as such:
obj = NumArray(nums)
obj.update(4,6)
obj.update(0,2)
obj.update(0,9)
print(obj.sumRange(4, 4))
obj.update(3,8)
print(obj.sumRange(0, 4))

