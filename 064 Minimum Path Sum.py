class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
            
        for i in range(1, m):
            for j in range(1, n):
                u = grid[i-1][j]
                l = grid[i][j-1]
                grid[i][j] = min(l + grid[i][j] , u + grid[i][j])
        
        return grid[m-1][n-1]


        
