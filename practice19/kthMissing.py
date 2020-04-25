class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """        
        start = nums[0]
        end = nums[-1]
        i = 0
        curr = nums[i]
        counter = 0
        while(i < len(nums)-1):
            if(nums[i+1] == curr + 1):
                curr = nums[i+1]
                i +=1 
            else:
                while(nums[i+1] != curr + 1):
                    counter += 1
                    if(counter == k):
                        return curr + 1
                    curr += 1
                curr = nums[i+1]
                i += 1

        return end + k - counter
        
        
a = Solution()
print(a.missingElement([4,7,9,10], 3))