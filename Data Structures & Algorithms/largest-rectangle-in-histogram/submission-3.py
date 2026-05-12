class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    
      
        stack=deque()
        n=len(heights)
        ans=0
       
        for i in range(len(heights)):
            start=i
            while stack and stack[-1][1]>heights[i]:
                index,height=stack.pop()
                ans=max(ans,height*(i-index))
                start=index
             
            stack.append((start,heights[i]))

      
        while stack:
            index,height=stack.pop()
            ans=max(ans,height*(n-index))
       
            
        
                
            #print(i,ans,leftSmaller[i],rightSmaller[i],heights[i]*(rightSmaller[i]-leftSmaller[i]-1))
        
        return ans
        





           # 4 1 2 3 5 6 1


