

class Solution(object):
    def plusOne(self,digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        
        else:
            for i in range(len(digits) - 1,-1,-1):
                
                if i == 0 and digits[i] == 9:
                    digits[i] = 0
                    digits = [1] + digits
                    return digits
                
                if digits[i] == 9:
                    digits[i] = 0
                    print(digits)
                    x = int(digits[i-1]) + 1
                    if x != 10:
                        digits[i-1] = str(int(digits[i-1]) + 1)
                        return digits
                    else:
                        continue
            
            
                         
                
