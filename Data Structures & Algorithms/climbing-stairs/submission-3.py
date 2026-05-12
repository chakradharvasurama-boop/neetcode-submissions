class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0 for i in range(n+1)]

        

        def backtrack(x):
            if x==n:
                return 1
            if x>n:
                return 0
            if dp[x]!=0:
                return dp[x]
            dp[x]= backtrack(x+1)+backtrack(x+2)
            return dp[x]
        return backtrack(0)




 

          
        return backtrack(n)
        
        
        



        