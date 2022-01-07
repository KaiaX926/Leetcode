# The core idea is to compare the letter one by one among all words in input until all the letters in the shortest word have been checked or at least a word has a different letter in the place.



class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        length = min([len(i) for i in strs])
        r = ''
        
        for i in range(length):
            add = strs[0][i]
            for j in strs:
                if j[i] != add:
                    return r
            r += add
        
        return r
