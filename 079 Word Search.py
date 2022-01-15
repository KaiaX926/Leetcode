class Solution(object):
    def exist(self,board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        l,w,lon = len(board),len(board[0]),len(word)
        for i in range(l):
            for j in range(w):
                if board[i][j] == word[0]:
                    passed = [[i,j]]
                    passed = self.checkpath(board,i,j,l,lon,w,word,1,passed)
                    if len(passed) == lon:
                        return True
        
        return False
    
    
    def checkpath(self,board,i,j,l,lon,w,word,index,passed):
        if len(passed) == lon:
            return passed
        
        possible = [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]
        for loc in possible:
            if loc[0] >= 0 and loc[0] < l and loc[1] >= 0 and loc[1] < w:
                if board[loc[0]][loc[1]] == word[index] and loc not in passed:
                    passed.append(loc)
                    index += 1
                    passed = self.checkpath(board,loc[0],loc[1],l,lon,w,word,index,passed)
                    if len(passed) == lon:
                        return passed
                    passed = passed[:-1]
                    index -= 1
        
        return passed
