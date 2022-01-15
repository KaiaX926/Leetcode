class Solution(object):
    
    def minWindow(self,s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_c = t
        dict_s = {}
        res = float('inf')
        for i in range(len(s)):
            if s[i] in t and s[i] in t_c:
                t_c = t_c.replace(s[i],'', 1)
                if s[i] not in dict_s:
                    dict_s[s[i]] = [i]
                else:
                    dict_s[s[i]].append(i)
            elif s[i] in t and s[i] not in t_c:
                dict_s[s[i]] = dict_s[s[i]][1:] + [i]
            
            if len(t_c) == 0:
                ans = list(dict_s.values())
                ans = [item for sublist in ans for item in sublist]
        
                start,end = min(ans),max(ans)
                if end - start < res:
                    res = end - start
                    r = s[start:end+1]
        

        if len(t_c) > 0:
            return ''
        
        return r
