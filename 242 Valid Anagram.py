class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dicts, dictt = {}, {}

        for i in range(len(s)):
            if s[i] not in dicts:
                dicts[s[i]] = 1
            else:
                dicts[s[i]] += 1
            
            if t[i] not in dictt:
                dictt[t[i]] = 1
            else:
                dictt[t[i]] += 1
            
        return sorted(dictt.items()) == sorted(dicts.items())
        
