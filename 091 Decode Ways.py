class Solution:
    
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        res = 0
        
        if len(s) == 0:
            res += 1
            return res
        
        for i in range(min(2,len(s))):
            if int(s[:i+1]) > 0 and int(s[:i+1]) <= 26 and s[0] != '0':
                #print(s[:i+1])
                res += self.numDecodings(s[i+1:])
                #print('res:',res)
        
        return res
       
    
        
