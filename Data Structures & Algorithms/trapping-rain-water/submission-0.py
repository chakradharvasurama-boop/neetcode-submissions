class Solution:
    def trap(self, height: List[int]) -> int:

        leftGreater=[]
        currLG=0
        for num in height:
            leftGreater.append(currLG)
            currLG=max(num,currLG)
        
        currRG=0
        ans=0
        for i in range(0,len(height)):
            num=height[len(height)-i-1]
            ans+=max(0,min(leftGreater[len(height)-i-1],currRG)-num)
            currRG=max(num,currRG)
        return ans


        