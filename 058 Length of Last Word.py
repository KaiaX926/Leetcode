class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        st,wt = 0,0
        for i in range(len(s)-1,-1,-1):
            print(s[i])
            if s[i] == ' ' and  wt > 0:
                return wt
            elif s[i] == ' ' and  wt == 0:
                st += 1
            else:
                print('add lentgh')
                wt += 1
        
        return wt
            
            
        
