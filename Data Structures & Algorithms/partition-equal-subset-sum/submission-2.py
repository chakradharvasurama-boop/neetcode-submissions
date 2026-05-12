class Solution:
    def canPartition(self, nums: List[int]) -> int:
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
        