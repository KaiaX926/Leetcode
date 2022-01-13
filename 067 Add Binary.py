class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        r = ''
        y = 0 
        while a or b:
            if a and b:
                x = int(a[-1]) + int(b[-1]) + y
            elif a:
                x = int(a[-1]) + y
            else:
                x = int(b[-1]) + y
                
            a,b = a[:-1],b[:-1]
            
            y = x//2
            m = x%2
            if m == 1:
                r = '1' + r
            elif m == 0:
                r = '0' + r
            
        print(y)
        if y == 0:
            return r
        else:
            while y != 0:
                m = y%2
                if m == 1:
                    r = '1' + r
                elif m == 0:
                    r = '0' + r
                y = y//2
            return r
            
            
                
                
            
