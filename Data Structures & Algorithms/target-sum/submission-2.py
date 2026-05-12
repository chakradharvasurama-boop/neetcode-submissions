class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        n=len(nums)
        dp=[defaultdict(int) for i in range(n+1)]
        dp[0][0]=1
        for i in range(n):
            for total,count in dp[i].items():

                dp[i+1][total-nums[i]]+=count
                dp[i+1][total+nums[i]]+=count
        return dp[n][target]
        '''


      
        n=len(nums)
        dp={}
        
        def backtack(i:int,curr:int)->int:
            if i==n:
                if curr==target:
                    return 1
                return 0
            if (i,curr) in dp:
                return dp[(i,curr)]
            dp[(i,curr)]=0
            
            dp[(i,curr)]+=backtack(i+1,curr-nums[i])
            dp[(i,curr)]+=backtack(i+1,curr+nums[i])
            return dp[(i,curr)]
        return backtack(0,0)
            

        