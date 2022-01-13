class Solution(object):
    def simplifyPath(self,path):
        """
        :type path: str
        :rtype: str
        """
        s,p,i = 0,0,1
        r = []
        w = path.split('/')
        for i in range(1,len(w)):
            if w[i] == '':
                continue
            elif w[i] == '..':
                r = r[:-1]
            elif w[i] == '.':
                continue
            else:
                r.append(w[i])
            
        res = '/'
        print(r)
        
        if len(r) == 0:
            return '/'
        
        if len(r) > 1:
            for i in range(len(r)-1):
                res += r[i]
                res += '/'
        
        res += r[-1]
        
        return res
