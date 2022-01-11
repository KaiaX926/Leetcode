class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ir = list(range(0,len(matrix)))
        jc = list(range(0,len(matrix[0])))
        ans = []
        while ir != [] and jc != []:
            i = ir[0]
            ir.remove(i)
            for q in jc:
                ans.append(matrix[i][q])
            j = jc[-1]
            jc.remove(j)
            for k in ir:
                ans.append(matrix[k][j])
            ir.reverse()
            jc.reverse()
            
        return ans
