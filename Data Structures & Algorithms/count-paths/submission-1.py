class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited=[[0 for i in range(n) ] for j in range(m)]
        dp=[[0 for i in range(n) ] for j in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i-1>=0:
                    dp[i][j]+=dp[i-1][j]
                if j-1>=0:
                    dp[i][j]+=dp[i][j-1]
        return dp[m-1][n-1]

        
'''
        def backtrack(i,j)-> int:
            if i==m-1 and j==n-1:
                #print("here")
               
                
                return 1

            if dp[i][j]:
                return dp[i][j]
            visited[i][j]=1
          
            
        
            if i+1<m and visited[i+1][j]!=1:
                dp[i][j]+=backtrack(i+1,j)
            if j+1<n and visited[i][j+1]!=1:
                dp[i][j]+=backtrack(i,j+1)
            visited[i][j]=0
            return dp[i][j]
        return backtrack(0,0)
        '''
        
        