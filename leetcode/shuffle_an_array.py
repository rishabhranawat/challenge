import random
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.pairs = {}
        for i in range(0, len(nums), 1):
            self.pairs[i] = nums[i]
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        for index, value in self.pairs.items():
            self.nums[index] = value
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        temp = self.pairs
        new = {}
        current = set()
        
        counter = 0
        while(len(current) != len(self.nums)):
            index = random.randint(0, len(self.nums)-1)
            val = self.pairs[index]
            if(val not in current):
                current.add(val)
                self.nums[counter] = val
                counter += 1
        return self.nums
        


# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_1 = obj.reset()
print(param_1)