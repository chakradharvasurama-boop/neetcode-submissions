class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
    
        

        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
       

        def helper(i,j):
            dp=nums.copy()
            dp[i+1]=max(dp[i],dp[i+1])
            for k in range(i+2,j+1):
                dp[k]=max(dp[k-1],dp[k]+dp[k-2])
            return max(dp[j],dp[j-1])

        
        return max(helper(0,n-2),helper(1,n-1))

        