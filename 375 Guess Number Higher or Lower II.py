class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def helper(a, b):
            if a >= b: return 0
            return min(x + max(helper(a, x-1), helper(x+1, b)) for x in range(a, b+1))
        return helper(1, n)
    
    
    def getMoneyAmount(self, n):
        need = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                need[lo][hi] = min(x + max(need[lo][x-1], need[x+1][hi])for x in range(lo, hi))
        return need[1][n]
