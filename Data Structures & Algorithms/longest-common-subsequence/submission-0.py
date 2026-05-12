class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1=len(text1)
        n2=len(text2)
        dp=[[-1]*(n2+1) for i in range(n1+1)]
        for i in range(n1+1):
            dp[i][n2]=0
        for i in range(n2+1):
            dp[n1][i]=0
        

        def backtack(i:int,j:int):
     
            if dp[i][j]!=-1:
                return dp[i][j]
       
            if text1[i]==text2[j]:
                
                dp[i][j]= 1+backtack(i+1,j+1)
            else:
                dp[i][j]= max(backtack(i+1,j),backtack(i,j+1))
            return dp[i][j]

        return backtack(0,0)
            


        