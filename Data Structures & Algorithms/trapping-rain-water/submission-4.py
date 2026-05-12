class Solution:
    def trap(self, height: List[int]) -> int:
        Gright=[]
        ans=0
        n=len(height)
        mr=-1
        for i in range(len(height)):
            Gright.append(mr)
            mr=max(mr,height[n-i-1])
        Gright.reverse()
        ml=-1
        for i in range(len(height)):
            ans+=max(0,min(Gright[i],ml)-height[i])
            ml=max(ml,height[i])


        return ans


            
        