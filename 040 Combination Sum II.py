class Solution(object):
    def combinationSum2(self,candidates, target):
        res = []
        candidates.sort()
        self.getPossibleSums(candidates, target, res)
        return res
    
    def getPossibleSums(self,candidates, target, res, op = []):
        if(target == 0) and op not in res:
            res.append(op)
            return

        if(target < 0):
            return
 
        for i in range(len(candidates)):
            if(i > 0 and candidates[i] == candidates[i - 1]):
                i += 1
                continue
            if(candidates[i] > target):
                break
            self.getPossibleSums(candidates[i+1: ], target - candidates[i], res, op + [candidates[i]])
