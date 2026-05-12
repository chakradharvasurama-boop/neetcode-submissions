class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceFromOrigin(x:int,y:int)->float:
            return math.sqrt(x*x+y*y)
        
        pq=[]

        for i,point in enumerate(points):
            heapq.heappush(pq,(-distanceFromOrigin(point[0],point[1]),i))
            if len(pq)>k:
                heapq.heappop(pq)


        ans=[]
        #print(pq)
        while pq:
            distance,index=heapq.heappop(pq)
            ans.append(points[index])
        ans.reverse()
        return ans

        