class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        for i in range(9):
            temp=set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in temp:
                        return False
                    temp.add(board[i][j])
        for i in range(9):
            temp=set()
            for j in range(9):
                if board[j][i]!='.':
                    if board[j][i] in temp:
                        return False
                    temp.add(board[j][i])

        def checkBox(r,c)->bool:
            temp=set()
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j]!='.':
                        if board[i][j] in temp:
                            return False
                        temp.add(board[i][j])
            
            return True
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not checkBox(i,j):
                    return False
        return True


        