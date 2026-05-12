class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols=len(board),len(board[0])

        queue=deque()

        for i in range(rows):
            if board[i][0]=="O":
                queue.append((i,0))
                board[i][0]="-"
            if board[i][cols-1]=="O":
                queue.append((i,cols-1))
                board[i][cols-1]="-"

        for i in range(1,cols-1):
            if board[0][i]=="O":
                board[0][i]="-"
                queue.append((0,i))
            if board[rows-1][i]=="O":
                queue.append((rows-1,i))
                board[rows-1][i]="-"
        
        while queue:
            r,c=queue.popleft()
            neighbors=[[0,1],[1,0],[-1,0],[0,-1]]
            for i,j in neighbors:
                if r+i==-1 or r+i==rows or c+j==-1 or c+j==cols or board[r+i][c+j]=='X' or board[r+i][c+j]=='-':
                    continue
                board[r+i][c+j]="-"
                queue.append((r+i,c+j))
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j]="X"
                if board[i][j]=='-':
                    board[i][j]="O"
                
        