class Solution:
    def trap(self, height: List[int]) -> int:
  
        ans=0
        l,r=0,len(height)-1
     
        ml=height[l]
        mr=height[r]
        while l<r:
            if height[l]<height[r]:

                ml=max(ml,height[l])
               
                ans+=ml-height[l]
                l+=1
                
                
                
                
            else:
                
                mr=max(mr,height[r])
                ans+=mr-height[r]
                r-=1
                
                
                
            #print(l,r,ans)



        return ans


            
        