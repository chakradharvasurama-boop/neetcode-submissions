class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distanceFromOrigin(x:int,y:int)->float:
            return math.sqrt(x**2+y**2)
        
        pq=[]

        for i,point in enumerate(points):
            heapq.heappush(pq,(distanceFromOrigin(point[0],point[1]),i))

        ans=[]
        print(pq)
        for i in range(k):
            distance,index=heapq.heappop(pq)
            ans.append(points[index])
        return ans

        