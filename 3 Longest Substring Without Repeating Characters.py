# Move rightward little by little until meeting the first duplicate character. 
# Locate the duplicate character in the past string and restart the exam process from that location.

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        m = 1
        
        if len(s) < 2:
            return len(s)
        
        while len(s) > m:
            r = []
            for i in range(len(s)):
                if s[i] not in r:
                    r.append(s[i])
                    if i + 1 == len(s):
                        return max(m,len(s))
                else:
                    try:
                        j = r.index(s[i])
                        s = s[j+1:]
                    except IndexError:
                        s = []
                        pass
                    m = max(m,len(r))
                    break
        
        return m
