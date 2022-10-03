class Solution:
    def isHappy(self, n: int) -> bool:
        return self.check(n,[])
        
    
    def check(self,num,history):
        if num == 1:
            return True
        elif num == 0:
            return False
        else:
            temp = list(str(num))
            ans = 0
            for num in temp:
                ans += int(num)**2
            if ans not in history:
                history.append(ans)
                return self.check(ans,history)
            else:
                return False
           
       
    
    
   
class Solution:
    def __init__(self):
        self.ans = []
        
    def isHappy(self, n: int) -> bool:
        n = sum([int(i)**2 for i in str(n)])
        if n == 1:
            return True
        elif n in self.ans:
            return False
        else:
            self.ans += [n]
            return self.isHappy(n)
        
