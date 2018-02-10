class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        empty_coords = []
        for i in range(0, len(grid), 1):
            for j in range(0, len(grid[1]), 1):
                if(grid[i][j] == '0'): empty_coords.append([i, j])
        
        max_kills = 0
        for coord in empty_coords:
            i = coord[0]
            j = coord[1]
            row = grid[i:]
            col = grid[:j]
            
            kills = 0
            up = i-1
            down = i+1
            
            while(up >= 0):
                if(grid[up][j] == "W"):
                    break
                elif(grid[up][j] == "E"):
                    kills += 1
                up -=1
            
            while(down < len(grid)):
                if(grid[down][j] == "W"):
                    break
                elif(grid[down][j] == "E"):
                    kills += 1
                down += 1
            
            left = j-1
            right= j+1
            
            while(left >= 0):
                if(grid[i][left] == "W"):
                    break
                elif(grid[i][left] == "E"):
                    kills += 1
                left -= 1
            
            while(right < len(grid[i])):
                if(grid[i][right] == "W"):
                    break
                elif(grid[i][right] == "E"):
                    kills += 1
                right += 1
            
            if(kills > max_kills): max_kills = kills
            
        return max_kills
a = Solution()
print(a.maxKilledEnemies([["0", "E", "0", "0"],["E", "0", "W", "E"], ["0", "E", "0", "0"]]))