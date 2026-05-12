class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rnextSmallest=[]
        lnextSmallest=[]
        stack=[]
        n=len(heights)
        ans=heights[0]
        for i in range(n): 
            currInd=i 
           
            while stack and stack[-1][1]>heights[i]:
                currInd=stack[-1][0]

                ans=max(ans,stack[-1][1]*(i-stack[-1][0]))
                stack.pop()
            stack.append((currInd,heights[i]))
        

        for i in range(len(stack)):
            ans=max(ans,stack[i][1]*(n-stack[i][0]))


      
       
        return ans
        
        
        
        

            

        