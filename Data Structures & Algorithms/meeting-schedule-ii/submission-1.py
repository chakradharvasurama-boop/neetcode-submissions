"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key= lambda x: x.start)
        n=len(intervals)
        if n==0:
            return 0
        roomNum=0
        pq=[]
        heapq.heappush(pq,intervals[0].end)
        for i in range(1,n):
            if pq[0]<=intervals[i].start:
                heapq.heappop(pq)
                
            heapq.heappush(pq,intervals[i].end)
             
        return len(pq)


        #0 6
        #5 20
        #15 100
        #16 30

        #20
        #16 30 

      
        