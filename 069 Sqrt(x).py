class Solution:
	def mySqrt(self, x):
		if x == 0 or x == 1: return x

		# directly start form 1
		l,r = 1,x
		while l <= r:
			mid = (l+r) // 2

			if mid * mid <= x < (mid + 1) * (mid + 1):
				return mid
			elif x < mid * mid:
				r = mid - 1
			else:
				l = mid + 1
