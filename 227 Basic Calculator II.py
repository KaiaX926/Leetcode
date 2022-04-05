class Solution:
    def calculate(self, s: str) -> int:
        def calculation(sym,a,b):
            if sym == '+':
                return a+b
            elif sym == '-':
                return a-b
            elif sym == '/':
                return a//b
            elif sym == '*':
                return a*b
            
        stack_num, stack_sym, syms =[], [], ['+', '-', '/', '*']
        temp = ''
        i = 0
        self.res = 0
        
        while i < len(s):
            if s[i] not in syms:
                temp += s[i]
                if i == len(s) -1:
                    stack_num.append(int(temp))
            else:
                stack_num.append(int(temp))
                stack_sym.append(s[i])
                temp = ''
            i += 1
        
        def priotity(stack_sym, stack_num, i):
            # print(stack_num,stack_sym)
            if len(stack_sym) > 1:
                if (stack_sym[i] == '+' or stack_sym[i] == '-') and (stack_sym[i+1] == '+' or stack_sym[i+1] == '-'):
                    temp = calculation(stack_sym[i], stack_num[i],stack_num[i+1])
                    stack_num = stack_num[:i] + [temp] + stack_num[i+2:]
                    stack_sym = stack_sym[:i] + stack_sym[i+1:]
                    priotity(stack_sym, stack_num, i)
                elif (stack_sym[i] == '+' or stack_sym[i] == '-') and (stack_sym[i+1] != '+' and stack_sym[i+1] != '-'):
                    priotity(stack_sym, stack_num, i+1)
                elif (stack_sym[i] == '/' or stack_sym[i] == '*'):
                    temp = calculation(stack_sym[i], stack_num[i],stack_num[i+1])
                    stack_num = stack_num[:i] + [temp] + stack_num[i+2:]
                    stack_sym = stack_sym[:i] + stack_sym[i+1:]
                    if i > 0:
                        priotity(stack_sym, stack_num, i - 1)
                    else:
                        priotity(stack_sym, stack_num, i)
            else:
                #print('final', stack_num,stack_sym)
                self.res = calculation(stack_sym[0], stack_num[0],stack_num[1])
                return 
        
        if not set(s) & set(syms):
            return int(s)
        priotity(stack_sym, stack_num, 0)
        return self.res

                
                
                
