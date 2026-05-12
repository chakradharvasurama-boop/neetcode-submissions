class Solution:
    def trap(self, height: List[int]) -> int:
  
        ans=0
        l,r=0,len(height)-1
     
        ml=height[l]
        mr=height[r]
        while l<r:
            if height[l]<height[r]:
                l+=1
                ml=max(ml,height[l])
                ans+=ml-height[l]
                
                
                
                
            else:
                r-=1
                mr=max(mr,height[r])
                ans+=mr-height[r]
                
                
                
            #print(l,r,ans)



        return ans


            
        