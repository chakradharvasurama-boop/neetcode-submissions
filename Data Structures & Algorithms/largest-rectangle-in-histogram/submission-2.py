class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    
        rightSmaller=[len(heights) for i in heights]
        stack=deque()
        n=len(heights)
        ans=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[n-i-1]:
                stack.pop()
            if stack:
                rightSmaller[n-i-1]=stack[-1]
            stack.append(n-i-1)
        stack.clear()
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            leftSmaller=stack[-1] if stack else -1
            stack.append(i)
       
            ans=max(ans,heights[i]*(rightSmaller[i]-leftSmaller-1))
        
                
            #print(i,ans,leftSmaller[i],rightSmaller[i],heights[i]*(rightSmaller[i]-leftSmaller[i]-1))
        
        return ans
        





           # 4 1 2 3 5 6 1


