class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        nums = sorted(nums)
        for i in range(0, len(nums), 1):
            total = nums[i]
            hi = len(nums)-1
            low = i+1
            while(hi > low):
                temp = nums[hi] + nums[low] + total
                if(temp > 0): hi -= 1
                elif(temp < 0): low += 1
                else:
                    n_triplet = [nums[i], nums[low], nums[hi]]
                    if(n_triplet not in triplets):
                        triplets.append(n_triplet)
                    low += 1
                    hi -= 1
        return triplets
                
a = Solution()
print(a.threeSum([-1, 0, 1, 2, -1, -4, -1]))