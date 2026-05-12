
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        queue=deque()
        queue.append((0,0))
        ans=0
        visited=[[0]*cols for _ in range(rows)]
        visited[0][0]=1
        while queue:
            for i in range(len(queue)):
                r,c=queue.popleft()
                if r==rows-1 and c==cols-1:
                    return ans
                neighbours=[[0,1],[1,0],[0,-1],[-1,0]]
                for dr,dc in neighbours:
                    if r+dr==-1 or c+dc==-1 or r+dr==rows or c+dc==cols or grid[r+dr][c+dc]==1 or visited[r+dr][c+dc]==1:
                        continue
                    visited[r+dr][c+dc]=1
                    queue.append((r+dr,c+dc))
            ans+=1
                    
                    
        return -1
        