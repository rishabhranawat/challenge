class TwoBIT:

    def __init__(self, nums):
        self.bit = self.generate(nums)
        self.nums = nums


    def next(self, index):
        complement = (~index)+1
        return (complement&index) + index

    def parent(self, index):
        complement = (~index)+1
        return index - (complement&index)

    
    def cumulative(self, row, col):
        x = row+1
        y = col+1
        cumu = 0
        while(x > 0):
            while(y > 0):
                cumu += self.bit[x][y]
                y -= (y & -y)
            x -= (x & -x)

        return cumu


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.bit = TwoBIT(matrix)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        pass
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.bit.cumulative(row2, col2)-self.bit.cumulative(row2, col1-1)\
        -self.bit.cumulative(row1-1, col2)+self.bit.cumulative(row1-1, col1-1)
        
class NumMatrix2(object):
    def __init__(self, matrix):
        if not matrix:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix, self.bit = [[0]*(self.n) for _ in range(self.m)], [[0]*(self.n+1) for _ in range(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
        print(self.bit)

    def update(self, row, col, val):
        diff, self.matrix[row][col], i = val-self.matrix[row][col], val, row+1
        while i <= self.m:
            j = col+1
            while j <= self.n:
                self.bit[i][j] += diff
                j += (j & -j)
            i += (i & -i)
        
    def sumRegion(self, row1, col1, row2, col2):
        return self.sumCorner(row2, col2) + self.sumCorner(row1-1, col1-1) - self.sumCorner(row1-1, col2) - self.sumCorner(row2, col1-1)
        
    def sumCorner(self, row, col):
        res, i = 0, row+1
        while i:
            j = col+1
            while j:
                res += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res    

# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

obj = NumMatrix(matrix)
print(obj.sumRegion(2, 1, 4, 3))
# obj.update(3,2,2)
# print(obj.sumRegion(2,1,4,3))