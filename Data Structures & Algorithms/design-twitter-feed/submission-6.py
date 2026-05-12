

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

        pointerMap={}
        for followee in self.followMap[userId]:
            pointerMap[followee]=len(self.tweetMap[followee])-1
        
        
        feed=[]
        for i in range(10):
            currMax=-1
            currpointer=-1
            currMaxTime=-1
            for followee in self.followMap[userId]:
                followeePointer=pointerMap[followee]
                if followeePointer>=0:
                    followeeTweetTime=self.tweetMap[followee][followeePointer][0]
                    if followeeTweetTime>currMaxTime:
                        currMax=followee
                        currpointer=followeePointer
                        currMaxTime=followeeTweetTime
            if currMax==-1:
                break
            #print(currMax)
            feed.append(self.tweetMap[currMax][currpointer][1])
            pointerMap[currMax]-=1


                
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
        
        
