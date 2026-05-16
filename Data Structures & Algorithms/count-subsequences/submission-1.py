class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[0]*(n+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][n]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i]==t[j]:
                    dp[i][j]+=dp[i+1][j+1]
                dp[i][j]+=dp[i+1][j]
        return dp[0][0]




'''
        m=len(s)
        n=len(t)
        dp=[[-1]*(n+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][n]=1
        for i in range(n):
            dp[m][i]=0


        def backtrack(i:int,j:int)->int:
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=0
            if s[i]==t[j]:
                dp[i][j]+=backtrack(i+1,j+1)
            dp[i][j]+=backtrack(i+1,j)
            return dp[i][j]
        return backtrack(0,0)
'''
            

        