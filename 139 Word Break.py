class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        str_len = len(s)
        dp = [False] * (str_len + 1)
    
        for i in range(1, str_len +1):
            for word in wordDict:
                if i == len(word):
                    if dp[i] == False:
                        dp[i] = s[0 : i] == word
            
                if i > len(word):
                    if dp[i] == False:
                        dp[i] = dp[i- len(word)] and s[i- len(word): i] == word
                    
        return dp[str_len]
