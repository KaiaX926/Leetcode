class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        x = [str(i) for i in range(1, n+1)]
        x.sort()
        return [int(i) for i in x]
