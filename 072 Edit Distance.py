# DP[0,0] = 0 # empty string to empty string
# DP[0,j] = j # j edits from empty string to w2[:j]
# DP[i,0] = i # i edits from w1[:i] to empty string
# since DP[i,j] only requires results from previous row and current row, reuse DP list size of (j+1) is enough




class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ls_1, ls_2 = len(word1), len(word2)
        dp = list(range(ls_1 + 1))
        for j in range(1, ls_2 + 1):
            pre = dp[0]
            dp[0] = j
            for i in range(1, ls_1 + 1):
                temp = dp[i]
                if word1[i - 1] == word2[j - 1]:
                    dp[i] = pre
                else:
                    dp[i] = min(pre + 1, dp[i] + 1, dp[i - 1] + 1)
                pre = temp
        return dp[ls_1]
        
