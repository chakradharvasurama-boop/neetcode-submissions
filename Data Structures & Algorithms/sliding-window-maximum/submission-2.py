#from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #[1,2,1,0,4,2,6]
        #10 9 8 7 6 5
        heap=[]
        ans=[]
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        ans.append(-heap[0][0])
        left=0
        for i in range(k,len(nums)):
            
            left+=1
            while len(heap)>0 and heap[0][1]<left:
                heapq.heappop(heap)
            heapq.heappush(heap,(-nums[i],i))
            #print(left,i,s[-1])
            ans.append(-heap[0][0])
        return ans


        