class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            
            grid[r][c] = 'W'
            
            dfs(r - 1, c) 
            dfs(r + 1, c) 
            dfs(r, c - 1)  
            dfs(r, c + 1)  
        
        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':
                    island_count += 1  
                    dfs(i, j)  
        
        return island_count
