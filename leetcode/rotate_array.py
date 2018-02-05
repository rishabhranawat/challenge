class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if(k%n == 0): return
        shifted = set()
        index = 0
        val = nums[0]

        while(len(shifted) <= n):
            shifted_to = (k+index)%n
            
            temp = nums[shifted_to]

            nums[shifted_to] = val
            val = temp
            
            shifted.add(index)

            counter = 0
            print(nums)
            while(shifted_to in shifted and counter < n-1):
                print(counter)
                shifted_to +=1
                val = nums[shifted_to]
                counter += 1

            index = shifted_to











            
a = Solution()
print(a.rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(a.rotate([1], 1))
print(a.rotate([1,2,3,4,5,6], 2))
print(a.rotate([1, 2], 0))