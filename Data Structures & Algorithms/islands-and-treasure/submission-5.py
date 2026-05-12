
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols=len(grid),len(grid[0])
        inf=2147483647
        visited=[[0]*cols for _ in range(rows)]
        queue=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    queue.append((r,c))
                    visited[r][c]=1
        
        while queue:
            r,c=queue.popleft()
            neighbors=[[0,1],[1,0],[-1,0],[0,-1]]
            for i,j in neighbors:
                if r+i==rows or c+j==cols or r+i==-1 or c+j==-1 or visited[r+i][c+j] or grid[r+i][c+j]==-1:
                    continue
                queue.append((r+i,c+j))
                grid[r+i][c+j]=1+grid[r][c]
                visited[r+i][c+j]=1
                






    

        