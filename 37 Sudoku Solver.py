# Return True/False in for loop will continue the loop.

def findPos(board, posDict):
        # find the "." in board
        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    posDict["row"] = row
                    posDict["col"] = col
                    return True
        return False
    
def isValid(board, row, col, num):
        # used in row already
        def usedRow(board, row, col, num):
            for col in range(9):
                if board[row][col] == str(num):
                    return True
            return False
        
        # used in col already 
        def usedCol(board, row, col, num):
            for row in range(9):
                if board[row][col] == str(num):
                    return True
            return False
        
        # used in box already
        def usedBox(board, row, col, num):
            for i in range(3):
                for j in range(3):
                    if board[row+i][col+j] == str(num):
                        return True
            return False
        
        # check if all conditions align 
        if not usedRow(board, row, col, num) and not usedCol(board, row, col, num) and not usedBox(board, row-row%3, col-col%3, num):
            return True
        return False
    
def solveSudoku(board):
        posDict = {"row":0,"col":0}
        times = 0
        print('times: ',times,'start!','-'*20)
        # if board is already full
        if not findPos(board,posDict): return True
        
        # position where we will fill the number
        row = posDict["row"]
        col = posDict["col"]
        print(posDict)
        
        # Check all 1-9 possiblities
        for num in range(1,10):
            if isValid(board, row, col, num):
                print('START FROM IS VALID!')
                print(row,col)
                board[row][col] = str(num)
                if solveSudoku(board):
                    print('yes')
                    return True
                board[row][col] = "."
                times += 1
        print('times: ',times)
                
        return False
        
   #----------------------------------------------------------------------------------
   def equal1(num):
    if num == 1:
        return True
    return False

def all_(l):
    for i in l:
        print(i)
        if equal1(i):
            return True
    
    return False
