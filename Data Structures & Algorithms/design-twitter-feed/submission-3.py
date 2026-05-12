class UserNode:
    def __init__(self,userId:int):
        self.userId=userId
        self.tweets=[]
        self.follows={}

class Twitter:

    def __init__(self):
        self.users={}
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not  in self.users:
            self.users[userId]=UserNode(userId)
        
        self.users[userId].tweets.append((self.time,tweetId))
        self.time+=1


        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not  in self.users:
            return []

        pq=[]
        user=self.users[userId]
        for time,tweet in user.tweets:
            heapq.heappush(pq,(time,tweet))
            if len(pq)>10:
                heapq.heappop(pq)
      
        for followee in user.follows.values():
            for time,tweet in followee.tweets:
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
        if followerId not  in self.users:
            self.users[followerId]=UserNode(followerId)
        if followeeId not  in self.users:
            self.users[followeeId]=UserNode(followeeId)

        self.users[followerId].follows[followeeId]=self.users[followeeId]
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId ==followeeId:
            return
        if followerId not  in self.users:
            self.users[followerId]=UserNode(followerId)
        if followeeId not  in self.users:
            self.users[followeeId]=UserNode(followeeId)
        if followeeId in  self.users[followerId].follows:
            self.users[followerId].follows.pop(followeeId)
        
