class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r=0,len(nums)-1
        n=len(nums)
        ans=nums[0]
       
       
        
       
        while l<=r:
            m=l+(r-l)//2
            
        
            if nums[l]<=nums[r]:
                return min(ans,nums[l])

            if nums[l]<=nums[m]:
                
                l=m+1
            else:
                ans=min(ans,nums[m])
                r=m-1
            
                 
        return ans
            


              



        return ans
        
        


        