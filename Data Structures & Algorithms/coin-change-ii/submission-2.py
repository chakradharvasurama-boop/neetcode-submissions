class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount==0:
            return 1
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n+1)]
        for i in range(amount+1):
            dp[n][i]=0
        for i in range(n+1):
            dp[i][amount]=1


        def backtack(i:int,curr:int)->int:
            #print(i,curr)
            if dp[i][curr]!=-1:
                return dp[i][curr]
            print(i,curr)

            dp[i][curr]=0
    
            dp[i][curr]+=backtack(i+1,curr)
            if curr+coins[i]<=amount:
                dp[i][curr]+=backtack(i,curr+coins[i])

                
            return dp[i][curr]
        return backtack(0,0)




            
        