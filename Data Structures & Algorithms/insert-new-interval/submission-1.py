
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        n=len(intervals)
        i=n-1
        while i>0 and intervals[i][0]<intervals[i-1][0]:
            intervals[i],intervals[i-1]=intervals[i-1],intervals[i]
            i-=1
        ans=[]
        start=intervals[0][0]
        end=intervals[0][1]
        #print(intervals)
        for i in range(1,n):
            #print(start,end)
            if intervals[i][0]>end:
                ans.append([start,end])
                start=intervals[i][0]
                end=intervals[i][1]
            else:
                end=max(end,intervals[i][1])
        ans.append([start,end])
       # print(ans)
        return ans
        #[[1,2],[3,5],[4,8][6,7],[8,10],[12,16]]


   


        