# The core idea is to build up a zero matrix and then update the elements in order, depending on the position of each character in the string s.
# The dimension of the zero matrix is calculated by the length of s. The column number is the number of groups that s can be divided into. Each group contains 2 times of the num of rows minus 2
# Then the location of each string can be decided by the order of it in each group and the group it's in.
# Finally fetch the elements in the updated matrix that is not zero.



class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        import numpy as np
        
        if len(s) == 1:
            return s
        
        if numRows == 1:
            return s
        
        group_num = numRows + numRows - 2 
        col_num = (len(s)//group_num + 1) * (numRows - 1) + 1
        r = np.zeros((numRows, col_num))
        r = r.astype(np.str)
        
        for i in range(len(s)):
            group = i//group_num
            loc = i%(group_num)
            col_min = group * (numRows - 1)
            
            if loc < numRows - 1:
                row,col = loc,col_min
                r[row,col] = s[i]
            else:
                col = loc - numRows + 1 + col_min
                row = numRows - 1 - (loc - numRows + 1)
                r[row,col] = s[i]
        
        result = ''
        print(r)
        for i in range(numRows):
            for j in range(col_num):
                if r[i,j] != '0.0':
                    result += r[i,j]
        
        return result
