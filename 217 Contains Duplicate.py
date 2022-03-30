import numpy as np
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(np.unique(nums)) != len(nums)
