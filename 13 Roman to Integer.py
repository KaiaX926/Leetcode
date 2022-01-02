# The core idea is to map each symbol to the corresponding number, check the sign, and sum them up.
# To decide whether the number we are adding to the final result is positive or negative, we compare it with the number on its left. If the current number is smaller, then its sign should be positive.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        num = [1,5,10,50,100,500,1000]
        symb = ['I','V','X','L','C','D','M']
        r = 0 
        
        for i in range(1, len(s) + 1):
            letter = s[-i]
            loc = symb.index(letter)
            add = num[loc]
            if i > 1:
                if symb.index(s[-i]) < symb.index(s[-i+1]):
                    add = -add
            r += add
        
        return r
