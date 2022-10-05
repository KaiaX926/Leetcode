 class Solution:
     def numSplits(self, s: str) -> int:
         prefix = []
         chars = set()
         for l in s:
             chars.add(l)
             prefix.append(len(chars))
        
         res = 0
         chars = set()
         for i in range(len(s)-1, 0, -1):
             chars.add(s[i])
             if len(chars) == prefix[i-1]:
                 res += 1
         return res
