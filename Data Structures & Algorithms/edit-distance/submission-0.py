class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*(m+1) for i in range(n+1)]
        dp[n][m]=0

        def backtrack(i:int,j:int)->int:

            if dp[i][j]!=-1:
                return dp[i][j]
            if i==n:
                dp[i][j]= m-j
                return dp[i][j]
            if j==m:
                dp[i][j]= n-i
                return dp[i][j]
            
            
            if word1[i]==word2[j]:
                dp[i][j]= backtrack(i+1,j+1)
            else:
                dp[i][j]= 1+min(backtrack(i,j+1),backtrack(i+1,j+1),backtrack(i+1,j))
            return dp[i][j]
        
        return backtrack(0,0)

        