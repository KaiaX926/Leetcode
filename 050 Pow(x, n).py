# The core idea is to update the rest of times to product the x as well as the x to save time.

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        y,curr = 1,abs(n)
        while curr > 0:
            if curr & 1 == 1:
                y *= x
            curr >>= 1
            x *= x
        
        if n >= 0:
            return y
        else:
            return 1/y
            
            
