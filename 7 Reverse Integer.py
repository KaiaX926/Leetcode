# The core idea is summing up each number multiplied by 10 to the power of the inverse location of the current number.
# First derive each number by taking the remainder of the original number minus the previous result multiplied by the corresponding number divided by the power of 10.
# For example, to fetch the number on the ones place, divide the x by 10. To fetch the number on the tens place, divide x minus one times the number on the ones place, so on and so forth.
# Then times each number by the inverse location of each number and sums them up.
# For example, the number on ones place needs to time the highest place and the number on the tens place needs to time the second-highest place.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        y = abs(x)
        z = len(str(y))+ 1
        r = 0
        
        if y < 10:
            return x
        
        for i in range(1,z):
            a = y % (10**i)
            r += a/(10**(i-1)) * (10**(z - i - 1))
            y -= a
            print(a,r)
        
        if r > 2**31:
            return 0
        elif x < 0:
            return -r
        else:
            return r
            
        
