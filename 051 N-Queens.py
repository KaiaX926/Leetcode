# The core idea is to use DFS and keep searching next possible move until all queues have been allocated. If the process has to end but there are less than n queens on the board, the process will relocate the last located queen. 


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        sols = []
        
        def dfs(times,state, pd, nd):
            print('times :',times)
            r = len(state)
            print(' '*times,state,pd,nd,'|',r)
            if r < n:
                for c in range(n):
                    print(' '*times,'---',c)
                    if c not in state and c-r not in pd and c+r not in nd:
                        times += 1
                        print(' '*times,'next step: ',times,state+[c], pd|{c-r}, nd|{c+r})
                        dfs(times,state+[c], pd|{c-r}, nd|{c+r})
                    
            else: 
                sols.append(state)
            
            times -= 1

    
        dfs(0,[], set(), set())
        res = []
        
        for sol in sols:
            a = []
            for p in sol:
                b = '.'*p + 'Q' + '.'*(n-p-1)
                a.append(b)
            res.append(a)
                
        return res #[[f"{'.'*p}Q{'.'*(n-p-1)}" for p in sol] for sol in sols]
        
