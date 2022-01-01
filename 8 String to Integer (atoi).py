# The core idea is to recognize the number and the sign in character using ASCII. The default sign is positive while if there's a '-' in the string, then change the sign to negative.
# The original output is 0. Update the output by multiplying the original number by 10 and adding the new digital.

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        r = 0
        sign = 1
        
        for i in range(len(s)):
            if ord(s[i]) < 48 or ord(s[i]) > 57:
                if ord(s[i]) == 45 and (ord(s[i+1]) >= 48 and ord(s[i+1]) <= 57):
                    sign = -1
            else:
                r = r*10 + int(s[i])
        
        if r*sign > 2**31 - 1:
            return 2**31 - 1
        elif r*sign < -2**31:
            return -2**31
        else:
            return r*sign
        
