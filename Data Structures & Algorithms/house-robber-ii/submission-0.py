class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
    
    
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp=nums.copy()

        nums[2]=max(nums[1],nums[2])
        for i in range(3,n):
            nums[i]=max(nums[i-1],nums[i]+nums[i-2])
            
        
        p1=max(nums[n-1],nums[n-2])
        dp[1]=max(dp[0],dp[1])
        for i in range(2,n-1):
            dp[i]=max(dp[i-1],dp[i]+dp[i-2])
        
        p2=max(dp[n-2],dp[n-3])
        return max(p1,p2)

        