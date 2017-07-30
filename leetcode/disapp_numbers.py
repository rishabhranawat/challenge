class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 1
        counter = 0
        miss = []
        nums = sorted(nums)
        s = set()
        while(counter < len(nums)):
            val = nums[counter]
            if(val not in s): 
                s.add(val)
            else: 
                counter += 1
                diff += 1
                if(counter == len(nums) and val - counter != diff):
                    miss.append(counter)
                continue
            if(val - counter != diff): 
                miss.append(counter+diff)
                diff = abs(val-counter)
            counter += 1
        return miss

a = Solution()
print(a.findDisappearedNumbers([2, 2]))