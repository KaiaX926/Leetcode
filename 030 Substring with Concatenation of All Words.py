# The core idea is to change the target word list and each possible subsets into a dictionary. Keys of the dictionary are words that have the same length. If two dictionaries are the same, then record the starting location of the current subset.
# The possible subset here means each substring in string s with the length that is the same as the combination of words in the target list.

class Solution(object):
    def findSubstring(self,s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        l = len(words[0])
        t = len(words)
        r = []
        dic_w = {}
        
        for item in words:
            if item not in dic_w:
                dic_w[item] = 1
            else:
                dic_w[item] += 1
         
        
        for i in range(len(s) - l * t + 1):
            a = s[i:i+l*t]
            b = {}
            while len(a) > 0:
                string = a[:l]
                if string not in words:
                    break
                elif string not in b:
                    b[string] = 1
                else:
                    b[string] += 1
                a = a[l:]
            if b == dic_w:
                r.append(i)
        
        return r
