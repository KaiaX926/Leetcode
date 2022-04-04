import numpy as np
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        long = min(len(matrix), len(matrix[0]))
        matrix = np.array(matrix).astype('int')

        for wid in range(long,0,-1):
            i,j = 0, 0
            for i in range(len(matrix) - wid + 1):
                for j in range(len(matrix[0]) - wid + 1):
                    print(i,j,wid)
                    if np.sum(matrix[i:i+wid,j:j+wid]) == wid**2:
                        return wid**2
        return 0
        
#############################################################################        
                        
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        cache = [[int(matrix[i][j]) if(i == 0 or j == 0) else 0 for j in range(n)] for i in range(m)]
        
        maxL = 0
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == '1' and i > 0 and j > 0):
                    cache[i][j] = min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1]) + 1
                maxL = max(cache[i][j], maxL)
        
                    
        return(maxL**2)                
