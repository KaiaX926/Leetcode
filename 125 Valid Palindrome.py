class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum())
        while s:
            if s[0].lower() == s[-1].lower():
                s = s[1:-1]
            else:
                return False
        
        return True
            
