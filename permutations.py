class Solution(object):
    permutations = list(list())
    def permuteBacktrack(self, counter, level, result, s):
        if(level == len(s)):
            r = []
            for each in result:
                r.append(each) 
            self.permutations.append(r)
            return
        for i in range(0, len(s), 1):
            if(counter[i] == 0):
                continue
            result[level] = s[i]
            counter[i] -= 1
            self.permuteBacktrack(counter, level+1, result, s)
            counter[i] += 1
            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.permutations = list(list())
        counter = [1]*len(nums)
        self.permuteBacktrack(counter, 0, [None]*len(nums), nums)
        return self.permutations

a = Solution()
print(a.permute([1, 2, 3]))