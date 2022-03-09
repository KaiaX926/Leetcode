class Solution:
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        if columnNumber <= 26:
            return chr(columnNumber+64)
        res = ""
        d = columnNumber
        while d > 26:
            d, m = divmod(d,26)
            if m != 0:
                res = chr(m+64) + res
            else:
                res = 'Z' + res
                d -= 1
        res = chr(d+64) + res
        return res
