class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={}
        for i in range(1,n+1):
            adj[i]=[]
        for t in times:
            adj[t[0]].append((t[1],t[2]))


        pq=[]
        shortest={}
        count=0
        heapq.heappush(pq,(0,k,k))
        minTime=-1
        
        while pq:
            distance,node,parent=heapq.heappop(pq)
            #print(count,distance,node,parent)
            
            
            if node in shortest:
                continue
            count+=1
            if count==n:
                minTime=distance
                break
            #print(adj[node])
            shortest[node]=(distance,parent)

            for nxt,nxtd in adj[node]:
                
                heapq.heappush(pq,(distance+nxtd,nxt,node))
        
        return minTime
        



        