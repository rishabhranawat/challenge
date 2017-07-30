class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1
        while(start <= end):
            su = numbers[start] + numbers[end]
            if(su == target): return [start+1, end+1]
            if(su < target):
                start += 1
            else:
                end -= 1
        return None

a = Solution()
print(a.twoSum([1, 2], 3))
print(a.twoSum([1, 2, 3, 4, 5, 6], 6))
print(a.twoSum([1, 4, 5, 6], 11))
print(a.twoSum([0,0,3,4], 0))