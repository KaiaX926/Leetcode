class Solution:
    def partition(self, s: str) -> List[List[str]]:
        temp,self.res,self.LL = [],[],len(s)
        
        def find(s,long,temp):
            if long <= len(s):
                if self.check(s[:long]):
                    find(s[long:],1,temp + [s[:long]])
                find(s,long+1,temp)
            else:
                L = sum(len(c) for c in temp)
                if L == self.LL:
                    self.res.append(temp)
            return
        
        find(s,1,[])
        return self.res
        
        
    def check(self,s):
        left, right = 0,len(s)-1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
