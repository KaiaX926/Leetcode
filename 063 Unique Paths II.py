class Solution(object):
    def uniquePathsWithObstacles(self,obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        
        row, col = len(obstacleGrid),len(obstacleGrid[0])
        
        board = [[0 for i in range(col)] for j in range(row)]
        
        board[0][0] = 1
        for j in range(1,col):
            if obstacleGrid[0][j] != 1:
                board[0][j] = 1
            else:
                break
        
        for i in range(1,row):
            if obstacleGrid[i][0] != 1: 
                board[i][0] = 1
            else:
                break
                
        print(board)
        
        for i in range(1,row):
            for j in range(1,col):
                #print(obstacleGrid[i][j])
                if obstacleGrid[i][j] != 1:
                    l = u = 0
                    if i-1 >= 0:
                        u = board[i-1][j]
                    if j-1 >= 0:
                        l = board[i][j-1]
                    board[i][j] = board[i-1][j] + board[i][j-1]
        print(board)
        return board[row-1][col-1]
