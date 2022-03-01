import numpy as np
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        diff = [a_i - b_i for a_i, b_i in zip(gas, cost)]
        
        for i in range(idx,len(diff)):
            #print(diff[i:] + diff[:i])
            sum_diff = np.cumsum(diff[i:] + diff[:i])
            if all(i >= 0 for i in sum_diff):
                return i

        return -1
        

#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
# 	    candidate, debit, credit = None, 0, 0
	
# 	    for i in range(len(gas)):
# 		    credit += gas[i] - cost[i]
# 		    if credit < 0:
# 			    candidate, debit, credit = None, debit - credit, 0
# 		    elif candidate is None: 
# 			    candidate = i

# 	    return candidate if credit >= debit else -1
