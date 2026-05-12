class Solution:
    def trap(self, height: List[int]) -> int:

        l,r=0,len(height)-1
        currLG=0
        currRG=0
        ans=0
        while(l<r):
            
            
            if height[l]<=height[r]:
                if currLG>height[l]:
                    ans+=max(0,min(currLG,height[r])-height[l])
                currLG=max(height[l],currLG)
                l+=1
            else:
                if currRG>height[r]:
                    ans+=max(0,min(currRG,height[l])-height[r])
                currRG=max(height[r],currRG)
                r-=1

        return ans


        