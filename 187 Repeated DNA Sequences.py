class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res,ans = {},[]
        for i in range(0,len(s)-9):
            if s[i:i+10] not in res:
                res[s[i:i+10]] = 1
            else:
                if s[i:i+10] not in ans:
                    ans.append(s[i:i+10])
        return ans     
 




#    def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         ans = []
#         left, right = 0, len(s)
#         while left < right and right-10 >= 0 and left+10 <= len(s):
#             if s[left:left+10] in s[left+1:] and s[left:left+10] not in ans:
#                 ans.append(s[left:left+10])
#             if s[right-10:right] in s[:right-1] and s[right-10:right] not in ans:
#                 ans.append(s[right-10:right])
#             left += 1
#             right -= 1
        
#         return ans     
    
    
    
    
#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         ans = []
#         for i in range(len(s)-10):
#             temp1 = s[:i]
#             temp2 = s[i+1:]
#             if (s[i:i+10] in temp1 or s[i:i+10] in temp2) and s[i:i+10] not in ans:
#                 ans.append(s[i:i+10])
        
#         return ans
