class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    
      
        stack=deque()
        n=len(heights)
        ans=0
       
        for i in range(n+1):
            start=i
            while stack and (i==n or stack[-1][1]>heights[i]):
                startIndex,height=stack.pop()
                ans=max(ans,height*(i-startIndex))
                start=startIndex
            if i!=n:
                stack.append((start,heights[i]))

      
      
            
        
                
            #print(i,ans,leftSmaller[i],rightSmaller[i],heights[i]*(rightSmaller[i]-leftSmaller[i]-1))
        
        return ans
        





           # 4 1 2 3 5 6 1
       



