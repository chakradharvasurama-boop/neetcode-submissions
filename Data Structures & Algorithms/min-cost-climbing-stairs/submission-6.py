class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        s=max(sum(cost),1)
        
        dp=[-1 for i in range(n)]
        
        def backtrack(x):
            if x>=n:
                return 0
            
            if dp[x]!=-1:
                return dp[x]

         



            dp[x]=cost[x]+min(backtrack(x+1),backtrack(x+2))
            return dp[x]
      
           
        return min(backtrack(0),backtrack(1))
        

        