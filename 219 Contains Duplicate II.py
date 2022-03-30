class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		# start a dict
        seen = defaultdict(list)
        for i,v in enumerate(nums):
            if v in seen:
                for x in seen[v]:
                    if abs(i-x)  <= k:
                        return True
                    
            seen[v].append(i)
            
        return False
