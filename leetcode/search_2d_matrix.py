class Solution(object):
    def searchRow(self, row, target):
        start = 0
        end = len(row)-1

        while(start <= end):
            mid = (start + end)/2
            if(row[mid] == target):
                return True
            if(row[mid] > target):
                end = mid-1
            else:
                start = mid+1
        return False
        
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if(len(row) == 0): continue
            if(row[0] == target): return True
            if(row[len(row)-1] == target): return True
            if(row[0] < target and row[len(row)-1] > target):  
                return self.searchRow(row, target)
        return False
            
a = Solution()
print(a.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 5))