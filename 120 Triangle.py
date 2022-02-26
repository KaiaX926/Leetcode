class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = triangle[0]
        
        def find(triangle,res):
            if not triangle:
                return min(res)
            
            curr,res_next = triangle[0],[]
            res_next.append(res[0] + curr[0])
            for i in range(1,len(curr)-1):
                res_next.append(min(res[i-1] + curr[i], res[i] + curr[i]))
            res_next.append(res[-1] + curr[-1])    
            
            return find(triangle[1:],res_next)
        
        return find(triangle[1:],res)
                
                
            
        
