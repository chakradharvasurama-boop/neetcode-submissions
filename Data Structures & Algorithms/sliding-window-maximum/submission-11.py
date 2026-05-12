class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p=[]
        ans=[]
        
        for i,num in enumerate(nums):
            heapq.heappush(p,(-num,i))
            #print(p[0])
            while p[0][1]<=i-k:
                heapq.heappop(p)
            if i>=k-1:
                ans.append(-p[0][0])
        return ans

            

        