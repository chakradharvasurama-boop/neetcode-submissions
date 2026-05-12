class Solution:
    def dfs(self,row: int,col: int, grid: List[List[str]],visit: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        if row==-1 or col==-1 or row==rows or col==cols or visit[row][col] or grid[row][col]=="0":
            return
    
        visit[row][col]=1
        self.dfs(row-1,col,grid,visit)
        self.dfs(row+1,col,grid,visit)
        self.dfs(row,col-1,grid,visit)
        self.dfs(row,col+1,grid,visit)

        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        rows,cols=len(grid),len(grid[0])
        visit=[[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and visit[i][j]==0:
                    count+=1
                    self.dfs(i,j,grid,visit)
        return count




        