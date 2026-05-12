class Solution:
    def trap(self, height: List[int]) -> int:
  
        ans=0
        l,r=0,len(height)-1
        mr=height[r]
        ml=height[l]
        while l<=r:
            if height[l]<height[r]:
                ans+=max(0,min(ml,mr)-height[l])
                
                l+=1
                ml=max(ml,height[l])
                
            else:
                ans+=max(0,min(ml,mr)-height[r])
                
                r-=1
                mr=max(mr,height[r])
            #print(l,r,ans)



        return ans


            
        