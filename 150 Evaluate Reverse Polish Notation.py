from collections import deque

class Solution:
    def calculate(self, a, token, b):
        if token == '*':
            res = int(a) * int(b)
        elif token == '+':
            res = int(a) + int(b)
        elif token == '-':
            res = int(a) - int(b)
        elif token == '/':
            res = int(a) / int(b)
            res = int(res)
        return str(res)
    
    def evalRPN(self, tokens: List[str]) -> int:
        # need to use stack!
        num_stck = deque()
        print('start: ',num_stck)
        
        for token in tokens:
            if token in ['+', '-', '/', '*']:
                a1 = num_stck.pop()
                a2 = num_stck.pop()
                # solution 1
                print(a2,token,a1)
                calcuated = self.calculate(a2, token, a1)
                # solution 2
                # expr = a2 + token + a1
                # calcuated = str(int(eval(expr)))
                num_stck.append(calcuated)
            else:
                num_stck.append(token)
        
        return num_stck[-1]
