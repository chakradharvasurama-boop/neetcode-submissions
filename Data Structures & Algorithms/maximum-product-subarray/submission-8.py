class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
 

        ans=nums[0]
        currMax,currMin=nums[0],nums[0]

        
        for i in range(1,n):
            currMax,currMin=max(nums[i]*currMax,nums[i]*currMin,nums[i]),min(nums[i]*currMax,nums[i]*currMin,nums[i])
            ans=max(currMax,ans)


            
        return ans

    
            




