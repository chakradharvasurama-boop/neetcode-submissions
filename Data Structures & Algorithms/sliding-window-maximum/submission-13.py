class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p=[]
        ans=[]
        q=deque()
        
        for i,num in enumerate(nums):
            
            while q and q[-1][0]<=num: 
                q.pop()
            q.append((num,i))
            #print(p[0])
            while q[0][1]<=i-k:
                q.popleft()
          
            if i>=k-1:
                ans.append(q[0][0])
        return ans

            

        