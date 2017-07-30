class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows = len(board)
        columns = len(board[0])
        total = 0

        counter = 0
        while(counter < len(board)):
            board[counter] = list(board[counter])
            counter += 1
        print(board)

        for row in range(0, rows, 1):
            for col in range(0, columns, 1):
                # Column wise Ship
                if(col+1 < columns and board[row][col+1] == 'X'):
                    for k in range(col, columns, 1):
                        if(board[row][k] == 'X'):
                            board[row][k] == '.'
                            if(k == columns-1):
                                total += 1
                        else:
                            total += 1
                            break
                    continue

                elif(row+1 < rows and board[row+1][col] == 'X'):

                    for p in range(row, rows, 1):
                        if(board[p][col] == 'X'):
                            board[p][col] = '.'
                            if(p == rows-1): total += 1
                        else:
                            total += 1
                            break
                    continue
                else:
                    right = row + 1
                    down = col + 1
                    if(right < rows and down < columns):
                        if(board[right][col] != 'X' and board[row][down] == 'X'):
                            total += 1
                    else:
                        if(rows == 1 and columns == 1):
                            total += 1
        return total
a = Solution()
# print(a.countBattleships(["X..X","...X","...X"]))
print(a.countBattleships(["XXX"]))