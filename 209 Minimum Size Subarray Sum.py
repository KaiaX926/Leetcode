class Solution:
	def minSubArrayLen(self, target: int, nums: List[int]) -> int:
		l = 0
		res = 0
		value = 0
		for r in range(len(nums)):
			value += nums[r]
        # I want to plus till it reach to target
			if value >= target and r - l == 0:
				return 1
        # for this line if the lenght is = 1 we can just return the answer
			while value >= target:
				if res == 0:
					res += r - l + 1
        #since at the starting res is equal to 0 so we need calulate the first res by ourself        
				value -= nums[l]
				l += 1
        #I wanna miuns the value until it is least than the target and compare the
        #----the new res with the old res.
				if value < target:
					res = min(res, r-l+2)
    
		return res
