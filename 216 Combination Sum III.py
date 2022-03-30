class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []
        if n > sum(list(range(9,9-k,-1))):
            return []
        
        def goback(s,k,temp,rest):
            s = temp[-1] + 1
            k += 1
            rest += temp[-1]
            temp = temp[:-1]
            return s,k,temp,rest
        
        def find(s,n,k,temp,rest):
            if s > min(n,9) or k < 0:
                s,k,temp,rest = goback(s,k,temp,rest)
            
            if k == 1:
                if rest >= s and rest <= min(n,9):
                    self.ans.append(temp + [rest])
                s,k,temp,rest = goback(s,k,temp,rest)
                
            if rest-s > 0:
                temp = find(s+1,n,k-1,temp + [s],rest-s)
            else:
                if len(temp) > 0:
                    s,k,temp,rest = goback(s,k,temp,rest)
                    temp = find(s,n,k,temp,rest)
                else:
                    return

        find(2,n,k-1,[1],n-1)
        return self.ans
