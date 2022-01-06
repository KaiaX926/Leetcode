
class Solution(object):
    def combinationSum(self,candidates, target):
        res = []
        candidates.sort()
        self.getPossibleSums(candidates, target, res)
        return res
    
    def getPossibleSums(self,candidates, target, res, op = []):
        if(target == 0):
            res.append(op)
            return

        if(target < 0):
            return
 
        for i in range(len(candidates)):
            if(candidates[i] > target):
                break
            self.getPossibleSums(candidates[i: ], target - candidates[i], res, op + [candidates[i]])
