class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {}
        cols = {}
        boxes = {}
        
        for each in board:
            print(each)
        counter = 0
        while(counter < 9):
            board[counter] = list(board[counter])
            counter += 1

        for k in range(0, 9, 1):
            rows[k] = []
            cols[k] = []

        for box in range(0, 9, 1):
            boxes[box] = []

        box = 1
        origBox = 1

        for row in range(0, 9, 1):
            if(row <= 2):
                box = 0
                origBox = box
            elif(row > 2 and row <= 5):
                box = 3
                origBox = box
            else:
                box = 6
                origBox = box

            for col in range(0, 9, 1):
                val = board[row][col]
                if(val != '.'):
                    if(val not in rows[row]):
                        rows[row].append(val)
                    else:
                        return False

                    if(val not in cols[col]):
                        cols[col].append(val)
                    else:
                        return False
                    
                    if(val not in boxes[box]):
                        boxes[box].append(val)
                    else:
                        return False
                if((col+1) % 3 == 0):
                    box += 1

        return True
        
a = Solution()

test1 = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
test2 = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
test3 = ["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]

print(a.isValidSudoku(test1))