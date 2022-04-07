class Solution:
    def countDigitOne(self, n):
        if n <= 0:
            return 0
    
        count, num, base, highbase = 0, n, 1, 10
    
        while num:
            num, mod = divmod(num, 10)
        
            if mod == 0:
                count += (n//highbase)*base
            elif mod == 1:
                count += (n//highbase)*base + (n%base + 1)
            else:
                count += (n//highbase)*base + base

            base *= 10
            highbase *= 10

        return count
