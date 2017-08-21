class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if(n == 0): return -1
        visited = set()
        
        counter = 0
        val = nums[counter]
        while(val not in visited):
            visited.add(val)
            if(val == target): 
                return counter % n
            else:
                counter += 1
                counter = counter % n
                val = nums[counter]
        return -1
            
        