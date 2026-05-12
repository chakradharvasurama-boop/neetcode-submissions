class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        ans=max(nums)
        m=min(nums)-1
        ans=nums[0]
        maxP,minP=nums[0],nums[0]

        
        for i in range(1,n):
            maxP,minP=max(nums[i]*maxP,nums[i]*minP,nums[i]),min(nums[i]*maxP,nums[i]*minP,nums[i])
            ans=max(maxP,ans)


            
        return ans

    
            




