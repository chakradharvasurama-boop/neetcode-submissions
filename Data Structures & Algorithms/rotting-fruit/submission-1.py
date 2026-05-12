class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])

        queue=deque()
        fresh=0
        time=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        
        while queue and fresh:
            l=len(queue)
            for _ in range(l):
                r,c=queue.popleft()

                neighbors=[[0,1],[1,0],[0,-1],[-1,0]]
                for i,j in neighbors:
                    if r+i==-1 or r+i==rows or c+j==-1 or c+j==cols or grid[r+i][c+j]!=1:
                       continue
                    queue.append((r+i,c+j))
                    grid[r+i][c+j]=2
                    fresh-=1
            time+=1
        
        return time if not fresh else -1

        