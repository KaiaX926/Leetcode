# The core idea is to check whether the number on each position from left to right is equal to the number on each position from left to right.
# Obtain number in normal order using string method and obtain the number in inverse order using calculation method. 
# The calculation method is to divide the original number by 10, keep the remainder. Then, update the original number by minus it by the remainder and dividing it by 10 for the next calculation.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        y = str(x)
        
        if x < 0:
            return False
        
        for i in range(len(y)//2):
            a = y[i]
            b = x % 10
            print(i,a,b)
            if a != str(b):
                return False
            x -= b
            x = x/10
            print(x)
        
        return True
