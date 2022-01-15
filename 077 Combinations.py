class Solution(object):
    def combine(self,n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return []
        
        res = [[i] for i in range(1,n+1)]
        res = self.find(res,n,k-1)
        
        return res


    def find(self,prefix, n, k): 
        if k == 0:
            res = prefix
            return res
            
        res=[]
        for item in prefix:
            #print(item)
            for i in range(max(item)+1,n+1):
                a = item[:]
                a.append(i)
                res.append(a)
        #print(res)
        res = self.find(res, n, k-1)
        return res



#-----------------------------------------------------------
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans= []
        for i in range(1,n+1):
            ans.append(i)
        return itertools.combinations(ans, k)
