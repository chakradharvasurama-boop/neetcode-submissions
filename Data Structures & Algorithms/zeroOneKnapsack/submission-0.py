class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n=len(profit)
        dp=[[-1]*(capacity+1) for i in range(n+1)]
        for i in range(capacity+1):
            dp[n][i]=0

        def backtrack(i:int,currWeight:int)->int:


            if dp[i][currWeight]!=-1:
                return dp[i][currWeight]

            if currWeight+weight[i]<=capacity:
                dp[i][currWeight]= max(profit[i]+backtrack(i+1,currWeight+weight[i]),backtrack(i+1,currWeight))
            else:
                dp[i][currWeight]= backtrack(i+1,currWeight)
            return dp[i][currWeight]
        return backtrack(0,0)
            

