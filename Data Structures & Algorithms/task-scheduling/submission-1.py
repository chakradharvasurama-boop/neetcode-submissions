class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap={}
        for task in tasks:
            hmap[task]=1+hmap.get(task,0)
        pq=[]
        temp=[]
        for task,count in hmap.items():
            heapq.heappush(pq,(-count,task))
            
        ans=0
        while pq:
            c=n+1
            while c and pq:
                count,node=heapq.heappop(pq)

                

                
                temp.append((count+1,node))

                c-=1

            while temp:
                count,node=temp.pop()
                if count!=0:
                    heapq.heappush(pq,(count,node))
            if pq:
                ans+=(n+1)
            else:
                ans+=(n+1-c)
            #print(ans)
          
            
        return ans
 
        #X -> Y -> idle -> X -> Y 2 
        #  

        #6 1 1 1 1 1 1
        #a b a c a d  a e a f a g
        #2 2 2 2 2 2 2 2 2 2 1
        