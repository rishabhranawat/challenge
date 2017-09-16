class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        red = 0
        white = 0
        blue = 0
        
        for each in nums:
            if(each == 0): red += 1
            elif(each == 1): blue += 1
            else:
                white += 1

        counter = 0
        while(red > 0):
            nums[counter] = 0
            red -= 1
            counter += 1

        while(blue > 0):
            nums[counter] = 1
            blue -= 1
            counter += 1
        
        while(white > 0):
            nums[counter] = 2
            white -= 1
            counter += 1
        
        print(nums)
                                
a = Solution()
a.sortColors([2, 0, 1, 1, 2, 2, 0, 1, 1])