# The core idea is to locate the row and then the column. If either qualified row or qualified column cannot be found, return False.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        loc = []
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                loc.append(i)
                break

        
        left,right = 0,len(matrix[i]) - 1
        while left <= right:
            if matrix[i][left] == target:
                loc.append(left)
                break
            if matrix[i][right] == target and matrix[i][left] != target:
                loc.append(right)
                break
            left += 1
            right -= 1
        
        if  len(loc) < 2:
            return False
        else:
            return True
            
