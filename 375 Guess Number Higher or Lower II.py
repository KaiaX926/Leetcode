class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def helper(a, b):
            if a >= b: return 0
            return min(x + max(helper(a, x-1), helper(x+1, b)) for x in range(a, b+1))
        return helper(1, n)
