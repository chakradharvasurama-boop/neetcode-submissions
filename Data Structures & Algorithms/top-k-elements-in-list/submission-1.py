class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
        heap=[]
        for key in d:
            heapq.heappush(heap,(d[key],key))
            if len(heap)>k:
                heapq.heappop(heap)
        
        ans=[]

        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
        