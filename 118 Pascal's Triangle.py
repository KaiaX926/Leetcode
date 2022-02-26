class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        def find(res,numRows):
            if numRows == 1:
                return res
            else:
                curr,temp = res[-1],[]
                for i in range(len(curr)-1):
                    temp.append(curr[i]+curr[i+1])
                temp = [1] + temp + [1]
                res.append(temp)
        
            return find(res,numRows - 1)
        
        return find(res,numRows)
        
        
        
