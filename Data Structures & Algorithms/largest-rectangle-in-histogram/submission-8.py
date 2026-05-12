class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rnextSmallest=[]
        lnextSmallest=[]
        stack=[]
        n=len(heights)
        ans=heights[0]
        for i,h in enumerate(heights): 
            start=i 
           
            while stack and stack[-1][1]>h:
                start=stack[-1][0]

                ans=max(ans,stack[-1][1]*(i-stack[-1][0]))
                stack.pop()
            stack.append((start,h))
        

        for i,h in stack:
            ans=max(ans,h*(n-i))


      
       
        return ans
        
        
        
        

            

        