class Solution:
    def trap(self, height: List[int]) -> int:
  
        ans=0
        l,r=0,len(height)-1
     
        ml=height[l]
        mr=height[r]
        while l<=r:
            if height[l]<height[r]:
                ans+=ml-height[l]
                
                l+=1
                ml=max(ml,height[l])
                
            else:
                ans+=mr-height[r]
                
                r-=1
                mr=max(mr,height[r])
            #print(l,r,ans)



        return ans


            
        