class Solution:
    def numTrees(self, n: int) -> int:
        #use divide and conquer to calculate the number of possible trees in left and right subtree
        #and for current root, the number of tree the the multiplication of left and right result
        #use memo to track the result for given i, j as the range
        #O(n^2) time and space
        
        memo = {}
        return self.dfs(1, n, memo)
    
    def dfs(self, start, end, memo):
        if (start, end) in memo:
            return memo[(start, end)]
        #none or single node
        if start >= end:
            return 1
        res = 0
        for i in range(start, end + 1):
            res += self.dfs(start, i - 1, memo)*self.dfs(i + 1, end, memo)
        memo[(start, end)] = res
        return res
#-----------------------------------------------------

# at each node i, steps to i = steps to j * steps from j to i
class Solution:
    def numTrees(self, n):
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, n + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]
