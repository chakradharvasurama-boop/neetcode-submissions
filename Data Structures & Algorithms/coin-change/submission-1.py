class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
        n=len(coins)
        dp=[-1 for i in range(amount+1)]

        dp[0]=0
        for i in range(1,amount+1):
            for j in range(n):
                if i-coins[j]>=0 and dp[i-coins[j]]!=-1:
                    if dp[i]==-1:
                        dp[i]=1+dp[i-coins[j]]
                    else:
                        dp[i]=min(dp[i],1+dp[i-coins[j]])
        return dp[amount]
        '''
        dp=[-2 for i in range(amount+1)]
        def backtrack(currAmount)->int:
            
            if currAmount<0:
                return -1
            if currAmount==0:
                return 0
            if dp[currAmount]!=-2:
                return dp[currAmount]

            dp[currAmount]=-1
            for i in range(n):
                p=backtrack(currAmount-coins[i])
                if p!=-1:
                    if dp[currAmount]==-1:
                        dp[currAmount]=1+p
                    else:
                        dp[currAmount]=min(1+p,dp[currAmount])


            return dp[currAmount]


            
        return backtrack(amount)
        '''
       

        