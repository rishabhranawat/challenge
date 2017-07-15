class Solution(object):
    def check(self, row, col, board, rowsn, colsn):
        liveNeighs = 0
        #up
        if(row + 1 < rowsn):
            if(board[row+1][col] == 1):
                liveNeighs += 1
                
        #down
        if(row - 1 >= 0):
            if(board[row-1][col] == 1):
                liveNeighs += 1
        
        #right
        if(col + 1 < colsn):
            if(board[row][col+1] == 1):
                liveNeighs += 1
        
        #left
        if(col - 1 >= 0):
            if(board[row][col-1] == 1):
                liveNeighs += 1
        
        #south east
        if(row + 1 < rowsn and col + 1 < colsn):
            if(board[row+1][col+1] == 1):
                liveNeighs += 1
        
        #north west
        if(row - 1 >= 0 and col - 1 >= 0):
            if(board[row-1][col-1] == 1):
                liveNeighs += 1
        
        #north east
        if(row - 1 >= 0 and col + 1 < colsn):
            if(board[row-1][col+1] == 1):
                liveNeighs += 1
        
        #south west
        if(row + 1 < rowsn and col - 1 >= 0):
            if(board[row+1][col-1] == 1):
                liveNeighs += 1

        curr = board[row][col]
        if(liveNeighs < 2):
            return False
        elif((liveNeighs == 2 or liveNeighs == 3) and curr == 1):
            return True
        elif(liveNeighs == 3 and curr == 0):
            return True
        elif(liveNeighs > 3):
            return False
        else:
            return False

        
        
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        tracker = {}
        
        rowsN = len(board)
        colsN = len(board[0])
        counter = 0
        for row in range(0, rowsN, 1):
            for col in range(0, colsN, 1):
                liveOrDie = None
                if(self.check(row, col, board, rowsN, colsN)):
                    liveOrDie = 1
                else:
                    liveOrDie = 0
                counter += 1
                tracker[counter] = [row, col, liveOrDie]
        
        for key, value in tracker.items():
            row = value[0]
            col = value[1]
            board[row][col] = value[2]