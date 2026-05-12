class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        s=max(sum(cost),1)
        
        dp=[-1 for i in range(n+1)]
        dp[0]=0
        dp[1]=0

        for i in range(2,n+1):
            dp[i]=min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
        return dp[n]

        '''
        def backtrack(x):
            if x>=n:
                return 0
            
            if dp[x]!=-1:
                return dp[x]

            dp[x]=cost[x]+min(backtrack(x+1),backtrack(x+2))
            return dp[x]
    
        return min(backtrack(0),backtrack(1))
        '''
        

        