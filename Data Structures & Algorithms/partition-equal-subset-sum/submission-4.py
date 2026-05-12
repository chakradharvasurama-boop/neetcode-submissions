class Solution:
    def canPartition(self, nums: List[int]) -> int:
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        n=len(nums)
        dp=[[0]*(target+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1


        for i in range(n-1,-1,-1):
            for j in range(target+1):
                dp[i][j]|=dp[i+1][j]
                if j-nums[i]>=0:
                    dp[i][j]|=dp[i+1][j-nums[i]]
        return bool(dp[0][target])
        '''
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        n=len(nums)
        dp=[[-1]*(total//2+1) for i in range(n+1)]
    
        def backtrack(i:int,s:int):
            if dp[i][s]!=-1:
                return dp[i][s]
            if s==0:
                dp[i][s]=1
                return dp[i][s]
            
            if i==n or s<0:
                dp[i][s]=0
                return dp[i][s]


            dp[i][s]= backtrack(i+1,s) or backtrack(i+1,s-nums[i])
            return dp[i][s]
            
        return bool(backtrack(0,target))
        
        '''


        '''
        total=sum(nums)
        n=len(nums)
        dp=[[-1]*(total+1) for i in range(n+1)]
    
        def backtrack(i:int,s:int):
            if dp[i][s]!=-1:
                return dp[i][s]
            if s!=0 and s != total and 2*s==total:
            
                    dp[i][s]=1
                    return dp[i][s]
            if i==n:
                dp[i][s]= 0
                return dp[i][s]
            
            
            
            dp[i][s]=backtrack(i+1,s+nums[i]) or backtrack(i+1,s)
            return dp[i][s]
        return bool(backtrack(0,0))
        '''
        