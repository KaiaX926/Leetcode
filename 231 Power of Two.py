class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print(n)
        if n == 0:
            return False
        elif n in (1,2):
            return True
        elif n % 2 == 0:
            return self.isPowerOfTwo(n//2)
