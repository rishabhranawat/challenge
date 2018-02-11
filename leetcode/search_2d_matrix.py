class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)-1
        col = 0

        while(row >= 0 and col < len(matrix[0])):
            val = matrix[row][col]
            if(val > target):
                row -= 1
            elif(val < target):
                col += 1
            else:
                return True
        return False
            
a = Solution()
print(a.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))