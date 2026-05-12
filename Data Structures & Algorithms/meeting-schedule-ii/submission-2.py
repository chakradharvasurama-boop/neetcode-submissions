"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
#1 2 3 4 5
#5 6 7 8 9
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts=[]
        ends=[]
        n=len(intervals)
        for i in range(n):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)
        starts.sort()
        ends.sort()
        s=0
        e=0
        count=0
        maxRooms=0
        while  e!=n:
            if s!=n and starts[s]<ends[e]:
                s+=1
                count+=1
                maxRooms=max(maxRooms,count)
            else:
                e+=1
                count-=1
        return maxRooms


        






        '''

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
        '''


        #0 6
        #5 20
        #15 100
        #16 30

        #20
        #16 30 

      
        