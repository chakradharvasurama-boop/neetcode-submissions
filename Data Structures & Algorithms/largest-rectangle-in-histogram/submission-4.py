class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    
      
        stack=deque()
        n=len(heights)
        ans=0
       
        for i in range(len(heights)):
            start=i
            while stack and stack[-1][1]>heights[i]:
                startIndex,height=stack.pop()
                ans=max(ans,height*(i-startIndex))
                start=startIndex
             
            stack.append((start,heights[i]))

      
        while stack:
            startIndex,height=stack.pop()
            ans=max(ans,height*(n-startIndex))
       
            
        
                
            #print(i,ans,leftSmaller[i],rightSmaller[i],heights[i]*(rightSmaller[i]-leftSmaller[i]-1))
        
        return ans
        





           # 4 1 2 3 5 6 1
       



