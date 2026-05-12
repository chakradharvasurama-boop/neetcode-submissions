class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rnextSmallest=[]
        lnextSmallest=[]
        stack=[]
        n=len(heights)
        ans=heights[0]
        for i in range(n-1,-1,-1):  
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                rnextSmallest.append(stack[-1])

            else:
                rnextSmallest.append(n)
            stack.append(i)

        stack=[]
        rnextSmallest.reverse()

        for i in range(n):
   
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                lnextSmallest.append(stack[-1])

            else:
                lnextSmallest.append(-1)
            stack.append(i)
            #print(lnextSmallest[i],rnextSmallest[i])
            ans=max(ans,heights[i]*(rnextSmallest[i]-lnextSmallest[i]-1))
        return ans
        
        
        
        

            

        