class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,cols=len(heights),len(heights[0])
        pacific=[[0]*cols for _ in range(rows)]
        atlantic=[[0]*cols for _ in range(rows)]

        ans=[]

        queue=deque()
   

        for i in range(cols):
            queue.append((0,i))
            pacific[0][i]=1
       

        for i in range(1,rows):
            queue.append((i,0))
            pacific[i][0]=1
     
        while queue:
            r,c=queue.popleft()
            neighbors=[[0,1],[1,0],[0,-1],[-1,0]]
            for i,j in neighbors:
                if r+i==-1 or r+i==rows or c+j==-1 or c+j==cols or pacific[r+i][c+j]==1 or heights[r+i][c+j]<heights[r][c]:
                    continue
                queue.append((r+i,c+j))
                pacific[r+i][c+j]=1
        for i in range(cols):
            queue.append((rows-1,i))
            atlantic[rows-1][i]=1
            if pacific[rows-1][i]:
                ans.append([rows-1,i])
        for i in range(0,rows-1):
            queue.append((i,cols-1))
            atlantic[i][cols-1]=1
            if pacific[i][cols-1]:
                ans.append([i,cols-1])
        while queue:
            r,c=queue.popleft()
            neighbors=[[0,1],[1,0],[0,-1],[-1,0]]
            for i,j in neighbors:
                if r+i==-1 or r+i==rows or c+j==-1 or c+j==cols or atlantic[r+i][c+j]==1 or heights[r+i][c+j]<heights[r][c]:
                    continue
                queue.append((r+i,c+j))
                atlantic[r+i][c+j]=1
                if pacific[r+i][c+j]:
                    ans.append([r+i,c+j])
        #print(pacific)
        #print(atlantic)
        return ans
        
        
            

        
        