# The core idea is to update result n times using the same function but the different input.

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        profix = '1'
        
        while n > 1:
            n -= 1
            profix = self.loop(profix)
                     
        return profix
    
    
    def loop(self,profix):
            
            r = ''
            i,count = 0,0
            print('input: ',profix)
            if profix == '1':
                return '11'
            
            while i < len(profix):
                if i == 0:
                    count = 1
                else:
                    if profix[i] == profix[i-1]:
                        if i != len(profix) - 1:
                            count += 1
                        else:
                            count += 1
                            r += str(count)
                            r += str(profix[i])
                    else:
                        if i != len(profix) - 1:
                            r += str(count)
                            r += str(profix[i-1])
                            count = 1
                        else:
                            r += str(count)
                            r += str(profix[i-1])
                            count = 1
                            r += str(count)
                            r += str(profix[i])
                i += 1
                
            return r    
        
