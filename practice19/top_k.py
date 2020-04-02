import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        data = {}
        for each in nums:
            if(each not in data):
                data[each] = 0
            data[each] += 1
        
        sorted_x = sorted(data.items(), key=lambda kv: kv[1], reverse=True)
        
        a = 0
        top = []
        for each in sorted_x:
            if(a == k):
                return top
            top.append(each[0])
            a += 1
        return top


a = Solution()
print(a.topKFrequent([4,1,-1,2,-1,2,3], 2))