class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n=len(intervals)

        start=intervals[0][0]
        end=intervals[0][1]
        res=[]
        for i in range(1,n):
            if intervals[i][0]>end:
                res.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
            else:
                end=max(intervals[i][1],end)
        res.append([start,end])
        return res


        