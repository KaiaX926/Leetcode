class Solution(object):
    
    def longestPalindrome(self,s):
        """
        :type s: str
        :rtype: str
        """
        
        pal = {}
        #l = s[0]
        s = '#'.join('{}'.format(s))
        #print(s)
        
        if len(s)<2:
            return s
        
        for i in range(len(s)-1):
            l = s[i]
            
            long = min(i,len(s)-1-i)
            #print(i,s[i],"long:",long)
            for j in range(long+1):
                if s[i-j] != s[i+j]:
                    break
                l = s[i-j:i+j+1]
                #print('l:',l)
                l = l.replace('#', '') 
                pal[l] = len(l)
            
            #print('-'*20)
        #print(pal)
        max_key = max(pal, key=pal.get)
            
        return max_key.replace('#', '') 
