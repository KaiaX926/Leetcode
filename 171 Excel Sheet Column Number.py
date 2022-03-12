class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ch = list(columnTitle)
        res = 0
        
        for i in range(len(ch)):
            res = res * 26 + (ord(ch[i]) - 64)
        
        return res
