from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) 
        res = 0
        
        def bfs(r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.appendleft((r,c))
            
            while queue:
                row, col = queue.pop()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    newr, newc = row + dr, col + dc
                    if (
                        newr >= 0 and newr < ROWS and 
                        newc >= 0 and newc < COLS and 
                        grid[newr][newc] == "1"
                    ):
                        grid[newr][newc] = "0"
                        queue.appendleft((newr, newc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    res += 1
        
        return res
                 
            
        
