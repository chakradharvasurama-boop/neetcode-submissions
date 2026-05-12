#from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #[1,2,1,0,4,2,6]
        #2:1 1:2
        #10 9 8 7 6 5
        ans=[]
        q=deque()
        for i in range(len(nums)):
            while len(q)>0 and q[-1][0]<=nums[i]:
                q.pop()
            q.append((nums[i],i))
            if i>=k-1:
                ans.append(q[0][0])
                if(q[0][1]==i-k+1):
                    q.popleft()

        return ans


        