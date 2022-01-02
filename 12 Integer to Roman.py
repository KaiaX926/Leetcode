# The core idea is to obtain the number on each place and convert it into roman symbol depending on it's relationship with 5 and 10.
# By keeping the remainder of the number divided by 10, we obtain the number to transform as well as the place of the number, like ones place, tens place, etc. 
# We need the position information to decide the key symbol we are using. 
# For example, if we are focusing on the number in ones place, then we should use the symbol "I" mainly, combing with others. If we are in the tens place, then we should use the symbol "X" mainly.
# Depneds on the interval that the number is located in, different combinations will be used. Since half of the interval has a special symbol, there are 4 intervals in total for each loop.
# Finally, update the roman symbol, calculated number, and the position pointer.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        r = ''
        i = 0
        symb = ['I','V','X','L','C','D','M']
        
        while num > 0:
            x = num % 10
            if x < 4:
                add = symb[i] * x
            elif x >= 4 and x < 5:
                add = symb[i] * (5 - x) + symb[i+1]
            elif x >= 5 and x < 9:
                add = symb[i+1] + symb[i] * (x - 5)
            else:
                add = symb[i] * (10 - x) + symb[i+2] 
                
            r = add + r    
            num -= x
            num = num/10
            i += 2
        
        return r
