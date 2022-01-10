# The core idea is to check the farthest place the pointer can go to at each step. In each step means checking each position that the pointer can be between the current pointer and the farthest place it can be.
class Solution(object):
    def jump(self, nums):
        l = r = res = farthest = 0
        while r < len(nums) - 1:
            for idx in range(l, r+1):
                farthest = max(farthest, idx + nums[idx])
            l = r+1
            r = farthest 
            res += 1
        return res
