class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        counter1 = 0
        counter2 = 0
        s = []
        if(n == 0): return
        counter = 0
        while(counter1 < m and counter2 < n):
            n1 = nums1[counter1]
            n2 = nums2[counter2]

            if(n1 < n2):
                s.append(n1)
                counter1 += 1
            else:
                s.append(n2)
                counter2 += 1
            counter += 1

        if(counter1 < m):
            while(counter1 < m):
                s.append(nums1[counter1])
                counter1 += 1

        if(counter2 < n):
            while(counter2 < n):
                s.append(nums2[counter2])
                counter2 += 1
        
        counter = 0
        while(counter < m+n):
            nums1[counter] = s[counter]
            counter += 1
        
a = Solution()
a.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
a.merge([1], 1, [], 0)
