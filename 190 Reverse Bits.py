class Solution:
    def reverseBits(self, n: int) -> int:
        f = str(bin(n))[2:]
        f = '0' * (32 - len(f)) + f
        return int(f[::-1],2)
