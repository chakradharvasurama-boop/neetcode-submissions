class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        ans=0
        while l<r:
            if heights[l]<heights[r]:
                ans=max(ans,heights[l]*(r-l))
                l+=1
            else:
                ans=max(ans,heights[r]*(r-l))
                r-=1

        return ans
