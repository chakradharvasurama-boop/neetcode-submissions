class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r=0,len(nums)-1
        n=len(nums)
        ans=nums[0]
        if n==1:
            return nums[0]
       
        
       
        while l<=r:
            
           
            if nums[l]<nums[r]:
                ans=min(nums[l],ans)
                break
            m=l+(r-l)//2
            ans=min(nums[m],ans)
                
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
                 
        return ans
            


              



        return ans
        
        


        