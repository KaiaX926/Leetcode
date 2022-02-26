class Solution:
    def maxProfit(self, prices: List[int]) -> int:        

        mini,maxi = prices[0],0
        for p in prices[1:]:
            maxi = max(p - mini,maxi)
            mini = min(p,mini)
        return maxi
