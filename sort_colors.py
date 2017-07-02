class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red = 0
        blue = 1
        white = 2
        
        counter = 0
        while(counter < len(nums)):
            if(nums[counter] == 0):
                if(red == -1): red = counter
                else:
                    temp = nums[red+1]
                    nums[red+1] = nums[counter]
                    red += 1
            elif(nums[counter] == 1):
                if(blue == -1): blue = counter
                else:
                    temp = nums[blue+1]
                    nums[blue+1] = nums[counter]
                    blue += 1
            elif(nums[counter] == 2):
                if(blue == -1): white = counter
                else:
                    temp = nums[white+1]
                    nums[white+1] = nums[counter]
                    white += 1
            counter += 1
        print(nums)
                     
a = Solution()
a.sortColors([2, 3, 1, 1, 2, 2, 3, 1, 1])