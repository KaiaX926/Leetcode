# The core idea is to check whether the string starts from the current place with the length equal to the needle is equal to the needle. If yes, return the location info. If else, move one step forward.
# Continue the loop until there are no more subsets with the length equal to the needle.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        l = len(needle)
        
        for i in range(len(haystack) - l + 1):
            s = haystack[i:i+l]
            if s == needle:
                return i
        
        return -1
