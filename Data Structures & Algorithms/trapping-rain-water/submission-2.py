class Solution:
    def trap(self, height: List[int]) -> int:

        l,r=0,len(height)-1
        currLG=height[l]
        currRG=height[r]
        ans=0
        while(l<r):
            if currLG<=currRG:
                l+=1
          
                ans+=max(0,min(currLG,height[r])-height[l])
                currLG=max(height[l],currLG)
                
            else:
                r-=1
                
                ans+=max(0,min(currRG,height[l])-height[r])
                currRG=max(height[r],currRG)
                

        return ans


        