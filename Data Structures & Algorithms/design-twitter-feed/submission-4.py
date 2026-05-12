

class Twitter:

    def __init__(self):
        self.followMap=defaultdict(set)
        self.tweetMap=defaultdict(list)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time,tweetId))
        self.time+=1


        

    def getNewsFeed(self, userId: int) -> List[int]:
     

        pq=[]
        
        for time,tweet in self.tweetMap[userId]:
            heapq.heappush(pq,(time,tweet))
            if len(pq)>10:
                heapq.heappop(pq)
      
        for followee in self.followMap[userId]:
            for time,tweet in self.tweetMap[followee]:
                heapq.heappush(pq,(time,tweet))
                if len(pq)>10:
                    heapq.heappop(pq)
        feed=[]
        #print(pq)
        while pq:
            feed.append(heapq.heappop(pq)[1])
        feed.reverse()
        return feed




        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId ==followeeId:
            return
        self.followMap[followerId].add(followeeId)

       
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId ==followeeId:
            return
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
        
