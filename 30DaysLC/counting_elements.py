class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        holder = [0 for x in range(0, max(arr))]

        counters = 0
        for each in arr:
        	holder[each-1] += 1
        for each in arr:
        	if(each <len(holder) and holder[each] > 0):
        		counters += 1
        return counters

a = Solution()
print(a.countElements([1,1,3,3,5,5,7,7]))
print(a.countElements([1,2,3]))
print(a.countElements([1,1,2,2]))
print(a.countElements([1,3,2,3,5,0]))