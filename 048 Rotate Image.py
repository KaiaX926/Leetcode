# The core idea is to flip the rows and then exchange the numbers on the symmetric positions.


class Solution(object):
    def rotate(self,matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l//2):
            for j in range(l):
                s = matrix[-i-1][j] + matrix[i][j]
                matrix[-i-1][j], matrix[i][j] = s - matrix[-i-1][j],s - matrix[i][j]
                
        for i in range(l):
            for j in range(i+1,l):
                s = matrix[i][j] + matrix[j][i]
                matrix[i][j], matrix[j][i] = s - matrix[i][j], s - matrix[j][i]
        
        return matrix
