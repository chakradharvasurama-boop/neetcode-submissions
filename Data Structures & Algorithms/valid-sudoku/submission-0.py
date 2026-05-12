class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def rowCheck(board:List[List[str]]) -> bool:
            for row in board:
                s=set()
                for item in row:
                    
                    if item in s:
                        return False
                    if ord(item)-ord('0')>=0 and ord(item)-ord('0')<=9:
                        s.add(item)
            return True
        
        def columnCheck(board:List[List[str]]) -> bool:
            for i in range(9):
                s=set()
                for j in range(9):
                    if board[j][i] in s:
                        return False
                    if board[j][i].isdigit():
                        s.add(board[j][i])
            return True
        def boxesCheck(board:List[List[str]]):
            ans=True
            def boxCheck(board,a,b):
                s=set()
                for i in range(3*a,3*a+3):
                    for j in range(3*b,3*b+3):
                        if board[i][j] in s:
                            return False
                        if board[i][j].isdigit():
                            s.add(board[i][j]) 
                return True  
            for i in range(3):
                for j in range(3):
                    ans=ans and boxCheck(board,i,j)
            return ans
        return rowCheck(board) and columnCheck(board) and boxesCheck(board)
                
        