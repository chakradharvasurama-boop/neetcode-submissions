
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n=len(profit)
        dp=[[-1]*(capacity+1) for i in range(n+1)]
        for i in range(capacity+1):
            dp[n][i]=0

        def backtrack(i:int,currCapacity:int)->int:
            if dp[i][currCapacity]!=-1:
                return dp[i][currCapacity]
            if currCapacity-weight[i]>=0:
            
                dp[i][currCapacity]= max(profit[i]+backtrack(i,currCapacity-weight[i]), profit[i]+backtrack(i+1,currCapacity-weight[i]),backtrack(i+1,currCapacity))
            else:
                dp[i][currCapacity]= backtrack(i+1,currCapacity)
            return dp[i][currCapacity]
        return backtrack(0,capacity)


