class BIT(object):
    def __init__(self, nums):
        self.nums = [0]*(len(nums))
        self.bit = [0]*(len(nums)+1)

    def next(self, index):
        complement = ~index+1
        return index + (complement&index)

    def parent(self, index):
        complement = ~index+1
        return index - (complement&index)

    def update(self, index, value):
        diff = value - self.nums[index]
        self.nums[index]=value

        index = index + 1
        next = index
        while(next < len(self.bit)):
            self.bit[next] += diff
            next = self.next(next)
        return True

    def cumulate(self, index):
        index = index + 1
        prev = index
        cumu = 0
        while(prev > 0):
            cumu += self.bit[prev]
            prev = self.parent(prev)
        return cumu

class Solution(object):

    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        n = len(flowers)
        bloomed = [1]*n

        bit = BIT(bloomed)
        dic = {}
        for i in range(0, len(flowers), 1):
            index = flowers[i]-1
            bit.update(index, 1)

            current = bit.cumulate(index)
            if(index+k+1 in dic):
                score = bit.cumulate(index+k+1)-current
                if(score == 1): return i+1
            if(index-k-1 in dic):
                score = current-bit.cumulate(index-k-1)
                if(score == 1): return i+1
            dic[index] = True
        return -1

a = Solution()
print(a.kEmptySlots([3, 1, 5, 4, 2], 1))
print(a.kEmptySlots([1,3,2], 1))
print(a.kEmptySlots([1,2,3], 1))