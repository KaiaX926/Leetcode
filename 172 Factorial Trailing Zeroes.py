import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = list(str(math.factorial(n)))
        i,res = len(r) - 1, 0 
        
        while i >= 0:
            if r[i] == '0':
                res += 1
                i -= 1
            else:
                return res
                
