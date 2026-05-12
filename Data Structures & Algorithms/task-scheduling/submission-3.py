class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap={}
        for task in tasks:
            hmap[task]=1+hmap.get(task,0)
        pq=[]
        tempq=deque()
        for task,count in hmap.items():
            heapq.heappush(pq,(-count))
            
        time=0
        while pq or tempq:
            time+=1
            if not pq:
                time=tempq[0][1]
                pq.append(tempq[0][0])
                tempq.popleft()
                continue
          
       
           
            Mcount=heapq.heappop(pq)
            Mcount+=1
            if Mcount:
                tempq.append((Mcount,time+n))
            if tempq and tempq[0][1]==time:
                heapq.heappush(pq,tempq.popleft()[0])

          
            
        return time
 
        #X -> Y -> idle -> X -> Y 2 
        #  

        #6 1 1 1 1 1 1
        #a b a c a d  a e a f a g
        #2 2 2 2 2 2 2 2 2 2 1
        