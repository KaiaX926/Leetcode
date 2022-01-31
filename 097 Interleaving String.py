class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1) + len(s2):
            return False
        
        self.visit = ()
        
        return self.findmatch(s1,s2,s3) or self.findmatch(s2,s1,s3)
        
    def findmatch(self,source,other,s3):
        if len(s3) == 0:
            if len(source) == 0 and len(other) == 0:
                return True
            else:
                return 
    
        else:
            for i in range(1,min(len(s3)+1,len(source)+1)):
                if source[:i] == s3[:i]:
                    if self.findmatch(other,source[i:],s3[i:]) is True:
                        return True
    
        return False
  
  # ---------------------------------------------------------------------------


# In dp(i, j) we keep 1 if it is possible to form string s3 upto i+j symbol from first i elements of s1 and first j elements of s2. 
# Every moment we need to check two at most two neighbors: dp(i, j - 1) and dp(i - 1, j): 
# we need to check if symbol s[i+j+1] is equal to s2[j] and answer is true for dp(i, j-1) and j >= 0, or similar condition for another string.


class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1)+len(s2)!=len(s3):
            return False
        
        dp={}
        
        def solve(i,j):
            
            if i== len(s1) and j==len(s2):
                return True
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if  i <len(s1) and s3[i+j]==s1[i] and solve(i+1,j):
                return True

            if j<len(s2) and s3[i+j]==s2[j] and solve(i,j+1):
                return True
            
            dp[(i,j)]=False
         
        return solve(0,0)
