# The core idea is to use stack to store the location info. The stack always start from the one location before the possible start location of a new substring.

class Solution(object):

    def longestValidParentheses(self,s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) < 2:
            return 0
        
        stack = [-1]
        m,n = 0,0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop(-1)
                if len(stack) == 0:
                    stack.append(i)
                else:
                    n = i - stack[-1]
                    m = max(m,n)
            #print(stack,m)
                    
        return m


#-------------------------------------------------------------------------------------------------
# Find how many valid pairs of '()' in the string

class Solution(object):

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) < 2:
            return 0
        
        profix = 0
        for i in range(len(s) - 1):
            if s[i] == '(' and s[i+1] == ')':
                s = s[:i] + s[i+2:]
                profix += 2
                break
                
        if profix == 0:
            s = []  
            
        profix += self.longestValidParentheses(s)
        return profix
