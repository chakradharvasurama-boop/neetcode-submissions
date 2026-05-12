

class Twitter:

    def __init__(self):
        self.followMap=defaultdict(set)
        self.tweetMap=defaultdict(list)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time,tweetId))
        self.time+=1


        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        pq=[]
     
        for followee in self.followMap[userId]:
            pointer=len(self.tweetMap[followee])-1
           
            if pointer>=0:
                time,tweet=self.tweetMap[followee][pointer]
                heapq.heappush(pq,(-time,tweet,followee,pointer))

        
        
        feed=[]
        
        while pq and len(feed)!=10:
            time,tweet,followee,pointer=heapq.heappop(pq)
            feed.append(tweet)
            if pointer-1>=0:
                nextTime,nextTweet=self.tweetMap[followee][pointer-1]
                heapq.heappush(pq,(-nextTime,nextTweet,followee,pointer-1))
        
        
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
        
        
