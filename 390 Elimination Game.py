class Solution:
    def eliminate(self, n, i):
        if n == 1:
            return 1
        if i%2 == 0 or n%2 != 0:
            return 2 * self.eliminate(n//2, i+1)
        return 2 * self.eliminate(n//2, i+1) - 1           
    
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.eliminate(n, 0)
