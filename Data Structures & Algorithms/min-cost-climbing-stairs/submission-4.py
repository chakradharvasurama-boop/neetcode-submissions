class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        s=max(sum(cost),1)
        
        dp=[[-1 for i in range(s*2)] for j in range(n*2)]

        def backtrack(x,total):
            if x>=n:
                return total

            if dp[x][total]!=-1:
                return dp[x][total]
            




            dp[x][total]= min(backtrack(x+1,total+cost[x]),backtrack(x+2,total+cost[x]))
            #print(x,total,dp[x][total])
            return dp[x][total]
        return min(backtrack(0,0),backtrack(1,0))

        