class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount==0:
            return 1
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][amount]=1
        for i in range(n-1,-1,-1):
            
            for j in range(amount-1,-1,-1):
                
          
    
                dp[i][j]+=dp[i+1][j]
                if j+coins[i]<=amount:
                    dp[i][j]+=dp[i][j+coins[i]]
                j-=coins[i]

        return dp[0][0]
        
        '''
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
        '''

'''
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

            dp[i][curr]=0
            temp=curr

            while temp<=amount:
                
                dp[i][curr]+=backtack(i+1,temp)

                temp+=coins[i]
            return dp[i][curr]
        return backtack(0,0)
'''


            
        