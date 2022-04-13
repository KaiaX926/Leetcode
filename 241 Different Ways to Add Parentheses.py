class Solution:
    def solve(self, s):
        if s.isdigit():
            return [int(s)]
        ans = []
        for i in range(len(s)):
            if s[i] in ["+", "-", "*"]:
                left = self.solve(s[:i])
                right = self.solve(s[i + 1:])
                for l in left:
                    for r in right:
                        if s[i] == "-": ans.append(l - r)
                        if s[i] == "+": ans.append(l + r)
                        if s[i] == "*": ans.append(l * r)
        return ans

    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.solve(expression)
