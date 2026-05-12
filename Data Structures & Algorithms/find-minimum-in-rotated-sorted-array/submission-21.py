class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r=0,len(nums)-1
        n=len(nums)
        if n==1:
            return nums[0]
       
        ans=nums[0]
       
        while l<=r:
            m=l+(r-l)//2
            ans=min(nums[m],ans)
            if nums[m]<nums[0] and nums[m]<nums[n-1]:
                r=m-1
            elif nums[m]>nums[0] and nums[m]>nums[n-1]:
                l=m+1
            elif nums[m]>nums[0] and nums[m]<nums[n-1]:
                r=m-1
            elif nums[m]<nums[0] and nums[m]>nums[n-1]:
                l=m+1
            elif nums[m]==nums[0]:
                l=m+1
            else:
                r=m-1



        return ans
        
        


        