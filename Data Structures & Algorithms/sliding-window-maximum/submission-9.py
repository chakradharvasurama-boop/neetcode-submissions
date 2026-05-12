#from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #[1,2,1,0,4,2,6]
        #2:1 1:2
        #10 9 8 7 6 5
        ans=[]
        q=deque()
        l,r=0,0
        while r<len(nums):
            while len(q)>0 and nums[q[-1]]<=nums[r]:
                q.pop()
            q.append(r)
            if r-l==k-1:
                ans.append(nums[q[0]])
                if(q[0]==l):
                    q.popleft()
                l+=1
            r+=1

        return ans


        