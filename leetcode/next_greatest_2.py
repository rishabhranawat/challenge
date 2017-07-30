class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        n = len(nums)
        for i in range(0, n, 1):
            index=i
            val =nums[index]
            counter = (index+1)%n
            if(counter == index): ret.append(-1)
            while(counter != index):
                if(nums[counter] > val):
                    ret.append(nums[counter])
                    break
                if((counter + 1) % n == index):
                    ret.append(-1)
                counter = (counter + 1)%n
        return ret
a = Solution()
print(a.nextGreaterElements([5, 4, 3, 2, 1]))