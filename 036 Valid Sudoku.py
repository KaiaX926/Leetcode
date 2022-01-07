# The core idea is to check each item in the matrix that whether it has appeared in the corresponding row or column or the small 3*3 board.

class Solution(object):
    def isValidSudoku(self, board):
        # row = [set()]*9
        # col = [set()]*9
        # box = [set()]*9
        
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                
                if value == ".":
                    continue
                    
                if value in row[i]:
                    return False
                row[i].add(value)
                
                if value in col[j]:
                    return False
                col[j].add(value)
                    
                
                boxID = (i//3)*3 + j//3####
                if value in box[boxID]:
                    return False
                box[boxID].add(value)

        return True
        
