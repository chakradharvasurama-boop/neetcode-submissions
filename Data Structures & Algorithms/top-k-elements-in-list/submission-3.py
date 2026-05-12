class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for num in nums:
            if num in hm:
                hm[num]+=1
            else:
                hm[num]=0
        pq=[(value,key) for key,value in hm.items()]
        heapq.heapify(pq)
        while len(pq)>k:
            heapq.heappop(pq)
        return [y for x,y in pq]
        