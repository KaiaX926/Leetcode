# The core idea is to use dynamic programming by changing the position of each pairs of numbers in order.

class Solution(object):
    def permute(self, nums):
        # DPS with swapping
        res = []
        if len(nums) == 0:
            return res
        self.get_permute(res, nums, 0)
        return res

    def get_permute(self, res, nums, index):
        if index == len(nums):
            res.append(list(nums))
            return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            # s(n) = 1 + s(n-1)
            self.get_permute(res, nums, index + 1)
            nums[i], nums[index] = nums[index], nums[i]
