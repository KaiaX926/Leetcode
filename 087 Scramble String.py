#geeksforgeeks.org/python-functools-lru_cache/

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        
        @lru_cache(None)
        def recurse(a, b):
            # base condition
            if a == b: return True
            if len(a) <= 1: return False 
            #(also takes care if a!=b and len(a) == 1== len(b))
            
            N = len(a) # both a and b have same len 
            for i in range(1,N):
                # condition 1: assume swapped
                contd1 = recurse(a[:i], b[-i:]) and recurse(a[i:], b[:-i])
                # condition 2: assume not swapped
                contd2 = recurse(a[:i], b[:i]) and recurse(a[i:], b[i:])
                
                if (contd1 or contd2):
                    return True
            
            return False        
            
        return recurse(s1, s2)   
                
            
        
