class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p=[]
        ans=[]
        q=deque()
        
        for i,num in enumerate(nums):
            
            while q and nums[q[-1]]<=num: 
                q.pop()
            q.append(i)
            #print(p[0])
            while q[0]<=i-k:
                q.popleft()
          
            if i>=k-1:
                ans.append(nums[q[0]])
        return ans

            

        