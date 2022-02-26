class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        
        def find(res,rowIndex):
            if rowIndex == 0:
                return res.pop()
            
            curr, temp = res[-1], []
            for i in range(len(res)-1):
                temp.append(curr[i] + curr[i+1])
            temp = [1] + temp + [1]
            res.append(temp)
            
            return find(res,rowIndex - 1)
        
        return find(res,rowIndex)
        
