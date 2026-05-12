class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)

        dp=[[-1,-1] for i in range(n+2)]
        dp[n][0],dp[n][1],dp[n+1][0],dp[n+1][1]=0,0,0,0
  
        
        def backtrack(i:int,bought:int)->int:
        
            if dp[i][bought]!=-1:
                return dp[i][bought]
            #print(i,bought)
            #print(i,dp[i][bought])
  
            if not bought:
                dp[i][bought]= max(backtrack(i+1,0),backtrack(i+1,1)-prices[i])


            else:
                dp[i][bought]= max(prices[i]+backtrack(i+2,0),backtrack(i+1,1))
            return dp[i][bought]
          

        return backtrack(0,0)


        '''
        n=len(prices)
        maxVal=max(prices)
        dp=[[-1]*(maxVal+2) for i in range(n+2)]
    
        for i in range(maxVal+2):
            dp[n][i]=0
            dp[n+1][i]=0

        def backtrack(i:int,bought:int)->int:
            if i>=n:
                return 0
            if dp[i][bought]!=-1:
                return dp[i][bought]
            if bought==maxVal+1:
               dp[i][bought]=max(backtrack(i+1,maxVal+1),backtrack(i+1,prices[i]))


            else:
              dp[i][bought]=max(prices[i]-bought+backtrack(i+2,maxVal+1),backtrack(i+1,bought))
            return dp[i][bought]

        return backtrack(0,maxVal+1)
        '''




        