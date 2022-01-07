# The core idea is to locate each number's place and sum up the products of numbers in lists one by one.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        r = 0
        
        for i in range(len(num1)): 
            for j in range(len(num2)): 
                r += int(num1[i]) * int(num2[j]) * 10**(len(num1) - i + len(num2) - j - 2) 
        
        return str(r)
