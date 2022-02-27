class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr,pro = prices[0], 0 
        for i in range(1,len(prices)):
            if prices[i] >  curr:
                pro += prices[i] - prices[i-1]
            curr = prices[i]
        
        return pro
