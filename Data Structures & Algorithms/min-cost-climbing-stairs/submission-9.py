class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        s=max(sum(cost),1)

        
      

        for i in range(n-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])
        return min(cost[0],cost[1])

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
        

        