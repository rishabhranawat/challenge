class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i in range(0, len(nums), 1):
            


        red = None
        blue = None
        white = None

        counter = 0
        n = len(nums)
        while(counter <n):
            color = nums[counter]
            if(color == 1):
                if(red == None):
                    red = counter
                else:
                    temp = nums[red+1]
                    nums[red+1] = color
                    nums[counter] = temp
                    red += 1
            counter += 1
        print(nums)
                     
a = Solution()
a.sortColors([2, 3, 1, 1, 2, 2, 3, 1, 1])