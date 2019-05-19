class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #[1, 2, 3, 4]
        n = str(len(nums)-1)
        product_zero_to_index = {}
        product_index_to_n = {}
        
        for i in range(0, len(nums), 1):
            key = "0"+str(i)
            prev_key = "0"+str(i-1)
            if(prev_key in product_zero_to_index):
                product_zero_to_index[key] = product_zero_to_index[prev_key] * nums[i]
            else:
                product_zero_to_index[key] = nums[i]
        
        #d = {00: 1, 01: 2, 02:6, 03:24}

        for j in range(len(nums)-1, -1, -1):
            key = str(j)+n
            prev_key = str(j+1)+n
            if(prev_key in product_index_to_n):
                product_index_to_n[key] = product_index_to_n[prev_key]*nums[j]
            else:
                product_index_to_n[key] = nums[j]
        
        #d2 = {03:24, 13:24, 23: 12, 33:4}

        result = []
        for j in range(0, len(nums), 1):
            pre_key = "0"+str(j-1)
            post_key = str(j+1)+n
            
            val = 1
            if(pre_key in product_zero_to_index):
                val *= product_zero_to_index[pre_key]
            if(post_key in product_index_to_n):
                val *= product_index_to_n[post_key]
            
            result.append(val)
        return result

s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
print(s.productExceptSelf([1, 0]))
print(s.productExceptSelf([1, 2, 3, 4, 5, 6, 6]))
            