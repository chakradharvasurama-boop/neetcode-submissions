import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq=[]
        
        for i in range(len(nums)):
            if i<k:
                heapq.heappush(self.pq,nums[i])
            elif nums[i]>self.pq[0]:
                heapq.heappop(self.pq)
                heapq.heappush(self.pq,nums[i])



                
        


        self.k=k
        

    
        
        

    def add(self, val: int) -> int:
       
        heapq.heappush(self.pq,val)
        if len(self.pq)>self.k:
            heapq.heappop(self.pq)
        

        

        return self. pq[0]
        
        
