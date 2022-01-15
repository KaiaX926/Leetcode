class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        col,row = [],[]
        l,w = len(matrix),len(matrix[0])
        
    
        for i in range(l):
            for j in range(w):
                # if j in col:
                #     matrix[i][j] = float('inf')
                if matrix[i][j] == 0:
                    col.append(j)
                    row.append(i)
        print(row,col)
        
        for i in range(l):
            for j in range(w):
                if i in row or j in col:
                    matrix[i][j] = 0
        
                    
        return matrix
        
