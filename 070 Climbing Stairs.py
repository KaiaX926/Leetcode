class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = [1,2]
        
        for i in range(n-2):
            res.append(res[i] + res[i+1])
        return res[-1]
    
        
