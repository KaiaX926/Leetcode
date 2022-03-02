class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        past = {}
        for i in range(len(nums)):
            if nums[i] in past:
                if past[nums[i]] == 1:
                    past[nums[i]] += 1
                else:
                    del past[nums[i]]
            else:
                past[nums[i]] = 1
        return list(past.keys())[0]
