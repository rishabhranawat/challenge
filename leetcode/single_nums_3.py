class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        counter = 0
        a = []
        while(counter < len(nums)):
            if(counter + 1 == len(nums)): 
                a.append(nums[counter])
            elif(nums[counter] == nums[counter+1]):
                counter += 2
            else:
                a.append(nums[counter])
                counter += 1

            if(len(a) == 2): return a
        return None
a = Solution()
print(a.singleNumber([-1,0]))