class Solution:

    def dfs(self,row: int,col: int, grid: List[List[int]],visit: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        if row==-1 or col==-1 or row==rows or col==cols or visit[row][col] or grid[row][col]==0:
            return 0
        count=1
        visit[row][col]=1
        count+=self.dfs(row-1,col,grid,visit)
        count+=self.dfs(row+1,col,grid,visit)
        count+=self.dfs(row,col-1,grid,visit)
        count+=self.dfs(row,col+1,grid,visit)
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans=0
        rows,cols=len(grid),len(grid[0])
        visit=[[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and visit[i][j]==0:
              
                    ans=max(self.dfs(i,j,grid,visit),ans)
        return ans
        