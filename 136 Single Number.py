class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        past = []
        for i in range(len(nums)):
            if nums[i] in past:
                past.remove(nums[i])
            else:
                past.append(nums[i])
        return past[0]
