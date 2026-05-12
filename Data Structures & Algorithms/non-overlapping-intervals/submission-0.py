class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        n=len(intervals)

        start=intervals[0][0]
        end=intervals[0][1]
        count=1
        res=[]
        for i in range(1,n):
            if intervals[i][0]>=end:
                start=intervals[i][0]
                end=intervals[i][1]
                count+=1
            else:
                end=min(intervals[i][1],end)
   
        return n-count
        
        